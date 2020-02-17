def convert(runtime_name):
    return {
            "MT"  : "MultiThreaded" ,
            "MTd" : "MultiThreadedDebug" ,
            "MD"  : "MultiThreadedDLL" ,
            "MDd" : "MultiThreadedDebugDLL"
    }[runtime_name]
