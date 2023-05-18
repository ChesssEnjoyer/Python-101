Client URL 
```
curl http://www.dataden.tech  ==  requests.get(utl)
```
Direct response content into output.html
```
curl -o uotput.html www.dataden.tech
```
Specify URL:
```
curl -s http://www.dataden.tech
```
More than one URL:
```
curl http://www.dataden.tech -next http://github.com
```
Methods in curl:
```
POST:
curl --data "name=John&surname=Doe" http://www.dataden.tech
curl --data '{"name":"John","surname":"Doe"}' \http://www.dataden.tech
curl -X POST -d "name=John&surname=Doe" http://www.example.com

PUT:
curl -X PUT -d "name=John&surname=Doe" http://www.example.com

PATCH:
curl -X PACHT -d "name=John&surname=Doe" http://www.example.com

DELETE:
curl -X DELETE -d "name=John&surname=Doe" http://www.example.com
```
We can use the _–include_ (_-i_) parameter to include the headers, and _–head_ (_-I_ -that’s capital ‘i’-) to include only the headers (calling the HEAD method).

Setting user-agent value:
```
curl --user-agent "Mozilla/4.73 [en] (X11; U; Linux 2.2.15 i686)" www.example.com
```

Timing a connection:
```
curl -w "%{time_total}\n" -o /dev/null -s www.example.com
```
