# airbnb

Simulating the life of an Analytics Engineer in Airbnb

## Prerequisites
Make sure to create a snowflake account with free credentials :)

To run this project have the following installed:
* [Pyenv](https://github.com/pyenv/pyenv)
* [Poetry](https://python-poetry.org)

## Installation
1. Clone 
```sh
   git clone https://github.com/luisricardo-ai/airbnb.git
```

2. Use the right version of Python for this project
```sh
    pyenv install 3.11
    pyenv local 3.11
```

3. Virtual Enviroment
```sh
    poetry env use $(pyenv which python)
    poetry env activate
```

4. Install dependencies
```sh
    poetry install
```

## How to run?

### Credentials

Take a look at `.env-example` and create a `.env` with your snowflake' credentials. 

The easiest way to get your **SNOWFLAKE_ACCOUNT** it's from the registration email that you received, go there and copy and paste the string before `.snowflakecomputing.com`. For example `abcde-fg123456` and keep in mind that sometimes urls include the `.aws` tag, too, such as `abcde-fg123456.aws`

https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-snowflake

Use the `profile.yml` example to copy and paste the content at your local `~/.dbt/profile.yml`. Make sure to use **YOUR_SNOWFLAKE_ACCOUNT**

---
### Creating snowflake user and database
To create the structure for snowflake you can run the code below. If you want to check the commands running behind the scenes, check the `app` folder

```cli
task create-snowflake
```

If you want to delete all the snowflake structure, run this.

```cli
task drop-snowflake
```


---
### Data Flow Progress
![DataFlowProgress](/img/data_flow_progress.png)