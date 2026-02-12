# Eneco Assignments

This is the readme for the assignments that were given to me from Eneco. 
In this file I will answer the questions in the assignments. If only code was needed i will explain how to run the script.

## assignment 1 
```
python assignment1.py
```

## assignment 2
```
bash assignment2.sh -f **result**s.csv
```

## assigment 3-1
```
python assignment3-1.py
```

What i found was that the only country that was missing was CI or Côte d'ivoire

## assignment 3-2
```
bash assignment3-2.sh
```

## assignment 4-1
```
python assignment4-1.py
```

| customer_type  | avg_total_sales |
| ------------- |:-------------:|
| Jazz Buyers | 38.964375 |
| Non-Jazz Buyers | 40.064444 |

What we found was that there is a negligible difference between Jazz buyer and non-Jazz buyers

## assignment 4-2
```
psql -U user_name -d database_name < assignment4-2.sql
```

using a function in the WHERE clause prevents PostgreSql from using a normal index on trach.name, so we need to change the column type to citext and create an index on it. 
This allows us to do a case-insensitive search without using a function in the WHERE clause, which improves performance.

## assignment 5
Seeing that it was divided into 3 sections using (.) it looks like a JWT. so i ran it through a JWT decoder and i got:

```
{
  "typ": "JWT",
  "alg": "RS256",
  "x5t": "nOo3ZDrODXEK1jKWhXslHR_KXEg",
  "kid": "nOo3ZDrODXEK1jKWhXslHR_KXEg"
}.{
  "aud": "https://Eneco.onmicrosoft.com/ecsaz-apigee-odp-t",
  "iss": "https://sts.windows.net/eca36054-49a9-4731-a42f-8400670fc022/",
  "iat": 1616416705,
  "nbf": 1616416705,
  "exp": 1616420605,
  "aio": "E2ZgYEg3Vdmf6hspv/uPMbff8/MCAA==",
  "appid": "1e0fb354-a78d-4f5b-9966-ed623a624599",
  "appidacr": "1",
  "idp": "https://sts.windows.net/eca36054-49a9-4731-a42f-8400670fc022/",
  "oid": "db6e89f9-db16-4252-9429-c4d5e48adabd",
  "rh": "0.AQUAVGCj7KlJMUekL4QAZw_AIlSzDx6Np1tPmWbtYjpiRZkFAAA.",
  "roles": [
    "ReadWoonEnergie",
    "ReadEneco",
    "ReadOxxio",
    "ReadEnecoBusiness",
    "ReadAll"
  ],
  "sub": "db6e89f9-db16-4252-9429-c4d5e48adabd",
  "tid": "eca36054-49a9-4731-a42f-8400670fc022",
  "uti": "SgBa7Q3KTUy3Qf8hzOY3AA",
  "ver": "1.0"
}.[Signature]
```

Here you can see the three sections with the first {} being the Header. the second {} being the payload and the last being the signature. 
JWT are used to transmit claims or identity information between 2 parties. 

## Assignment 6
For this assignment i used different scripts to find the flags so here is what I did and the flag that i found

### 1
base64 decode RkxBR3s3Mjc0ZTVkYy1hYjYwLTRmYzItOGY1MS1lZTZlY2ViNmJlZjd9

**result**:FLAG{7274e5dc-ab60-4fc2-8f51-ee6eceb6bef7}

### 2
```
grep -Eno 'FLAG\{[^}]+\}' airports.csv runways.csv countries.csv
```

**result**: countries.csv:54:FLAG{e9cade1a-55a8-4af5-887d-a70ac0f3078a}

### 3
```
grep -Eno 'FLAG\{[^}]+\}' country_data.json
```

**result**: 41:FLAG{d90ef201-1a5b-495a-ac90-44da0e5c49b1}

### 4
```
dig code001.ecsbdp.com TXT
```

**result**: ;; ANSWER SECTION:
        code001.ecsbdp.com.     10800   IN      TXT     "FLAG{2f0056e5-cac9-4ad5-87e9-dfea199f40f6}"

### 5
Using the code for assignment 4-1 I added in the query variable this query
```
SELECT proname, prosrc
FROM pg_proc
WHERE prosrc ~ 'FLAG\{[^}]+\}';
```

**result**: 0  show_flag  \n  BEGIN\n    -- FLAG{b5c8d8be-419a-4757-8310-f1c7b1cabd5f}\n    RETURN 'Almost..!';\n  END\n

### 6
Using this code to run through all the http responses for the different countries
```
import requests
import pandas as pd
import re

FLAG = re.compile(r"FLAG\{[^}]+\}")
countries = pd.read_csv('countries.csv',keep_default_na=False)
iso =countries["code"].dropna().unique()

url = "http://code001.ecsbdp.com/countries/"

for code in iso: 
    full_url = url + code
    response = requests.get(full_url)

    flag_header = response.headers.get("X-Code-Flag")

    if flag_header and FLAG.search(flag_header):
        print(code)
        print(flag_header)
```

**result**: PL
        FLAG{184b6747-6871-49a3-b953-11dd23006097}


## Found flags
    FLAG{7274e5dc-ab60-4fc2-8f51-ee6eceb6bef7}
    FLAG{e9cade1a-55a8-4af5-887d-a70ac0f3078a}
    FLAG{d90ef201-1a5b-495a-ac90-44da0e5c49b1}
    FLAG{2f0056e5-cac9-4ad5-87e9-dfea199f40f6}
    FLAG{b5c8d8be-419a-4757-8310-f1c7b1cabd5f}
    FLAG{184b6747-6871-49a3-b953-11dd23006097}



