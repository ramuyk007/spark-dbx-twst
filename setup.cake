#load nuget:?package=ce.devops.scripts.build.cake&version=0.1.508-ceda-6127-pyspar0026&prerelease=true
Environment.SetupDefaultEnvironmentVariables(Context);

BuildParameters.SetParameters(context: Context,
                            buildSystem: BuildSystem,
                            sourceDirectoryPath: "./src",
                            title: "offeringname.pipelinename");


PythonSetup.SetPythonParameters(pythonCoverageXMLFileNameWithOutExtension: "coverage",
							pythonTestReportsXMLFileNameWithOutExtension: "testreports",
							unitTestDirectoryPath: "/repo/src/_tests_/unit", 				
							appDirectoryPath: "/repo/src/app"); 							
                                    
Build.RunPySpark();
