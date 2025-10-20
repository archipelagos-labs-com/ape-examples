<picture align="center">
  <img alt="Pandas Logo" src="./ArchipelagosLabsLogo.png">
</picture>


# APE: Analytics Platform for the Environment

## 1. Introduction

Provides examples of using the APIs and endpoints available for Analytics Platform for the Environment (APE). There are currently two ways accessing APE programmatically, via a Python package thats wraps all calls made to the platform and unpacks the messages received back, and using a JSON based HTTP REST API.

Where possible we would encourage users to make use of the Python package. This is because the package uses a binary format for all requests and responses, which can prove more efficient than JSON when relatively large amount of data are returned, such as when data published by one or more IoT devices is requested.

The JSON based REST API should meet the needs of most users wishing to consume data from the platform. As described above, while JSON  is not as well suited when dealing with large amounts of data, this potential issue can easily be circumvented by requesting data for a smaller number of devices or for a constrained time period.

## 2. Python Package

The Python package can be installed using <a href=https://pypi.org/project/pip/>Pip</a> from the Archipelagos Labs package repository. The <i>config</i> subfolder of the <i>python</i> folder there is a <i>requirements.txt</i> file listing the dependencies required to run examples, and a <a href=https://docs.conda.io/projects/conda/en/stable>Conda</a> environment file that can be used to create a new environment using that package manager. 

The <i>scripts</i> subfolder of the <i>python</i> there are Windows Batch files and Bash scripts that may be used to build a Conda environment using the environment file described above, and to update an existing environment should the contents of the environment file be modified at any point in the future.

Once a suitable virtual or conda environment has been created, the Python scripts located in the <i>src</i> subfolder or the <i>python</i> folder can be run as standalone Python scripts within such an environment. The scripts are named to reflect their purpose, although please also see the comment at the very top of each script for further details.

The credentials used to access the platform, and the URL of the Data Service component that the Python package sends requests to, can be directly supplied as parameters to the login function and constructor of the Client class, used in the various example Python scripts provided in the <i>src</i> subfolder of the <i>python</i> folder. 

This information can also be supplied in an <i>ape.toml</i> file, an example of which is given in the <i>config</i> subfolder of the <i>python</i> directory. This Python package attempts to locate this file in 3 locations: if an environment variable APE_CONFIG_DIR is defined then it looks in the directory specified by this variable, if not found it then looks in the current working directory, and if still not found it looks in the <i>.ape</i> subdirectory of the user's home directory.     


## 3. JSON REST API

The JSON REST API may be used in all modern programming languages and Microsoft Excel; including the following: Python, C#, Java, and C++. Data may also be requested from the command line using a tool such as <a href=https://curl.se/>curl</a>, which is readily available on all modern operating systems, including Windows, Linux, and MacOS.

The <i>scripts</i> subfolder of the <i>json</i> folder there are Windows Batch files and Bash scripts that may be used to send requests using curl. In the <i>src</i> subfolder of the <i>json</i> folder there are example Python scripts that use the JSON REST API and only require the <a href=https://pypi.org/project/requests/>requests</a> package as a dependency, and do not use the APE Python package.  

The <i>excel</i> subfolder of the <i>json</i> folder there are Microsoft Excel spreadsheets that provide examples of retrieving device data and metadata (i.e. concerning the devices defined for a specified tenant). Please follow the instructions in these spreadsheets as values need to be provided in certain cells to allow them to connect to APE. 
