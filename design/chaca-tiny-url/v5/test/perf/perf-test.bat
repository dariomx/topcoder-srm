ECHO OFF
CLS
SET PATH=C:\Users\dbahena\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin;%PATH%;
SET PATH=C:\Users\dbahena\Anaconda2;C:\Users\dbahena\Anaconda2\Scripts;%PATH%;
cd c:\Users\dbahena\PycharmProjects\topcoder-srm\design\chaca-tiny-url\v5\test\perf
ECHO welcome to chaca-tiny-url testing
ECHO ---
ECHO ON

locust --host=http://c-tu.net -f perf-test1.py