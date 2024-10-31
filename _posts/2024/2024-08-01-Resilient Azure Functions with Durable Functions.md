---
title: Resilient Azure Functions with Durable Functions
author: matt
categories: [Public]
classification: Public
tags: [cloud]
date: 2024-08-01 22:29:58 
likes: 1
---

*Durable Functions* is a feature of [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview) that lets you write stateful functions in a serverless compute environment. The extension lets you define stateful workflows by writing *[orchestrator functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-orchestrations)* and stateful entities by writing *[entity functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-entities)* using the Azure Functions programming model. Behind the scenes, the extension manages state, checkpoints, and restarts for you, allowing you to focus on your business logic. [1]

## Key Concepts

1. **Durable Functions**: Allows writing stateful functions in a serverless environment, enabling workflows that can resume from the last known state.
2. **State Persistence**: Store the state (e.g., last processed ID) in durable storage like Azure Table Storage or Cosmos DB.
3. **Exception Handling**: Implement robust exception handling to ensure workflows can resume from the last checkpoint.
4. **Idempotency**: Ensure operations can be retried without adverse effects or duplications.

## Implementing Resilient Workflows

Durable Function workflow consists primarily of an Orchestrator Function and one or more Activity Functions. Multiple activities can be chained together in sequence, with contextual information optionally being passed from one activity to another in the chain.

The following examples describe the Function Chaining pattern described in [1]. The examples all target the Azure Function Isolated Worker Model.

### Orchestrator Function example for Isolated Worker Model

```csharp
using Microsoft.DurableTask;
using Microsoft.Azure.Functions.Worker;
using System.Threading.Tasks;

public class OrchestratorFunction
{
    [Function("OrchestratorFunction")]
    public static async Task RunOrchestrator([OrchestrationTrigger] TaskOrchestrationContext context)
    {
        ActivityStatus lastProcessingStatus = new ActivityStatus
        {
            LastProcessedId = "initialId",
            ProcessingStatus = ProcessingStatus.New,
            ProcessingStage = ProcessingStage.ActivityOne,
            LastUpdated = DateTime.UtcNow
        };

        try
        {
	        lastProcessingStatus = await context.CallActivityAsync<ActivityStatus>("ActivityOne", lastProcessingStatus);

	        // save processing state...
	        lastProcessingStatus.ProcessingStatus = ProcessingStatus.New;
	        lastProcessingStatus.ProcessingStage = ProcessingStage.ActivityTwo;

	        lastProcessingStatus =  await context.CallActivityAsync<ActivityStatus>("ActivityTwo", lastProcessingStatus);

	        // save processing state...
	        lastProcessingStatus.ProcessingStatus = ProcessingStatus.New;
	        lastProcessingStatus.ProcessingStage = ProcessingStage.ActivityThree;

	        lastProcessingStatus = await context.CallActivityAsync<ActivityStatus>("ActivityThree", lastProcessingStatus);
	        
	        // save processing state...
        }
        catch (Exception ex)
        {
            // Handle exception
        }
    }
}
```

### Activity Function Example for Isolated Worker Model

```csharp
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;
using System;
using System.Threading.Tasks;

public class ActivityFunctions
{
    private readonly ILogger _logger;

    public ActivityFunctions(ILoggerFactory loggerFactory)
    {
        _logger = loggerFactory.CreateLogger<ActivityFunctions>();
    }

    [Function("ActivityOne")]
    public async Task<ActivityStatus> ActivityOne([ActivityTrigger] ActivityStatus lastProcessingStatus, ILogger log)
    {
        try
        {
	      Logger.LogInformation("Migrating records...");

	      if (status.ProcessingStage != ProcessingStage.ActivityOne)
	      {
	        Logger.LogInformation($"Last processing state has stage of '{status.ProcessingStage}', passing through...");
	        return status;
	      }
	      else
	      {
	        status.ProcessingStatus = ProcessingStatus.InProgress;
	      }

		  // Processing logic

	      // update processing status...
	      Logger.LogInformation($"All work done. Status moved to '{ProcessingStatus.Complete}'");
	      status.ProcessingStatus = ProcessingStatus.Complete;
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error migrating records.");
            throw; // Re-throw to ensure the orchestration knows about the failure
        }
    }
}
```

### Program.cs Configuration for Isolated Worker Model

An easy way to persist additional state is via Azure Table Storage - configure the TableServiceClient as descibed below.

```csharp
using Azure.Data.Tables;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var host = new HostBuilder()
    .ConfigureFunctionsWorkerDefaults()
    .ConfigureServices(services =>
    {
        services.AddSingleton(new TableServiceClient(Environment.GetEnvironmentVariable("AzureWebJobsStorage")));
        services.AddSingleton<OrchestratorFunction>();
    })
    .Build();

host.Run();
```

## Summary

By leveraging Azure Durable Functions, you can implement resilient, stateful workflows in a serverless environment. Proper handling of state, robust exception handling, and idempotent operations ensure your functions can gracefully recover from failures and continue processing from the last known good state.

### References

\[1\] Durable Functions Overview \- Azure \| Microsoft Learn\]\(https://learn\.microsoft\.com/en\-us/azure/azure\-functions/durable/durable\-functions\-overview\)