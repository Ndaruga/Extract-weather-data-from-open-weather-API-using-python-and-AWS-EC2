# Extract weather data from OpenWeatherMap using python and AWS EC2
This is a project on extracting weather data from the OpenWeatherMap API using Python and AWS EC2. The process involves creating an account on OpenWeatherMap and getting an API key, installing the requests library for Python, creating a Python script that makes a request to the OpenWeatherMap API, passing the API key to the request, specifying the city or location for which you want to get weather data, getting the response from the API, parsing the response to get the weather data, saving the weather data to a file, and deploying the Python script to AWS EC2.


## Step 1: Creating an EC2 Instance
Login to your AWS account here: https://console.aws.amazon.com/ <br><br>
Under <strong>Services</strong> or on the search bar, select or search for `EC2`<br><br>
Click `Launch an instance`
> 1. Provide a name for your server
> 2. Under <strong>Application and OS images</strong> select `Ubuntu` <br><br>![image](https://github.com/Ndarugaa/Extract-weather-data-from-open-weather-API-using-python-and-AWS-EC2/assets/68260816/a05aecca-e843-463e-833a-8217f81d495b)<br><br>
> 3. Under <strong>instance type</strong>, select `t2.micro` family instance
> 4. As for <strong>Key Pair (login)</strong>, click on `Create new Key pair`<br>A create key pair wizard appears <br>![image](https://github.com/Ndarugaa/Extract-weather-data-from-open-weather-API-using-python-and-AWS-EC2/assets/68260816/a87c0472-9869-4346-b391-61c6c4f4eb8a) <br><br> Provide a name for your key pair and click `create`
> 5. A `<key-pair_name.pem>` file is downloaded to your local machine.
> 6. In <strong>Network Settings</strong> under <strong>Firewall (Security Groups)</strong>, you can choose to let AWS `create security group` for you or you can `select existing security group`. <br>Whichever method you choose make sure you `allow SSH traffic from my IP` or from `Anywhere`
> 7. Click on `Launch Instance`


## Step 2: Connect EC2 instance remotely with VS Code (Optional)


## OpenWeatherMap API
