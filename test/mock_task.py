default_json_task = {
    "uuid":  "e4af4f1f-32ae-4e78-8d1b-1b9d8260d78b",
    "name":  "test",
    "shortname":  "e4af4f1f-32ae-4e78-8d1b-1b9d8260d78b",
    "profile":  "docker-batch",
    "poolUuid":  None,
    "jobUuid":  None,
    "progress":  100,
    "runningInstanceCount":  0,
    "runningCoreCount":  0,
    "executionTime":  "00:28:04",
    "wallTime":  "00:30:27",
    "state":  "Success",
    "previousState":  "UploadingResults",
    "instanceCount":  1,
    "stateTransitionTime":  "2021-07-20T16:40:13Z",
    "previousStateTransitionTime":  "2021-07-20T16:40:07Z",
    "lastModified":  "2021-07-20T16:40:13Z",
    "creationDate":  "2021-07-20T16:09:43Z",
    "endDate":  "2021-07-20T16:40:13Z",
    "waitForPoolResourcesSynchronization":  None,
    "resourceBuckets":  [
        "resource"
    ],
    "advancedResourceBuckets":  [
    ],
    "resultBucket":  "result",
    "errors":  [
    ],
    "completedInstances":  [
        {
            "results":  [
                "s3://storage.qarnot.com/result/data-result.txt"
            ],
            "instanceId":  0,
            "wallTimeSec":  1827.2825,
            "execTimeSec":  1684,
            "execTimeSecGHz":  5385.8447,
            "peakMemoryMB":  0,
            "state":  "Success",
            "error":  None,
            "cpuModel":  "AMD Ryzen 7 2700 Eight-Core Processor",
            "coreCount":  16,
            "clockRatio":  0.999,
            "averageGHz":  3.198245
        }
    ],
    "status":  {
        "timestamp":  "0001-01-01T00:00:00Z",
        "lastUpdateTimestamp":  "0001-01-01T00:00:00Z",
        "downloadProgress":  0,
        "executionProgress":  100,
        "uploadProgress":  100,
        "instanceCount":  0,
        "downloadTime":  "00:00:00",
        "downloadTimeSec":  0,
        "environmentTime":  "00:01:02",
        "environmentTimeSec":  62,
        "executionTime":  "00:28:04",
        "executionTimeSec":  1684,
        "executionTimeByCpuModel":  [
            {
                "model":  "AMD Ryzen 7 2700 Eight-Core Processor",
                "time":  1684,
                "core":  16
            }
        ],
        "executionTimeGhzByCpuModel":  [
            {
                "model":  "AMD Ryzen 7 2700 Eight-Core Processor",
                "timeGhz":  5385.8447265625,
                "clockRatio":  0.999,
                "core":  16
            }
        ],
        "uploadTime":  "00:00:04",
        "uploadTimeSec":  4,
        "wallTime":  "00:30:27",
        "wallTimeSec":  1827,
        "succeededRange":  "0",
        "executedRange":  "0",
        "failedRange":  "",
        "startedOnceRange":  "0",
        "runningInstancesInfo":  {
            "perRunningInstanceInfo":  [
            ],
            "snapshotResults":  [
            ],
            "timestamp":  "0001-01-01T00:00:00Z",
            "averageFrequencyGHz":  0,
            "maxFrequencyGHz":  0,
            "minFrequencyGHz":  0,
            "averageMaxFrequencyGHz":  0,
            "averageCpuUsage":  0,
            "clusterPowerIndicator":  1,
            "averageMemoryUsage":  0,
            "averageNetworkInKbps":  0,
            "averageNetworkOutKbps":  0,
            "totalNetworkInKbps":  0,
            "totalNetworkOutKbps":  0,
            "runningCoreCountByCpuModel":  [
            ]
        }
    },
    "snapshotInterval":  0,
    "resultsCount":  1,
    "constants":  [
        {
            "key":  "DOCKER_REPO",
            "value":  "qlab/pandas"
        },
        {
            "key":  "DOCKER_TAG",
            "value":  "latest"
        },
        {
            "key":  "DOCKER_CMD",
            "value":  "python3 launch.py"
        }
    ],
    "tags":  [
    ],
    "dependencies":  None,
    "autoDeleteOnCompletion":  False,
    "completionTimeToLive":  "00:00:00",
    "maxRetriesPerInstance":  0
}