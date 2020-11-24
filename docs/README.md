# IMaC_startkit
Infrastructure Management as Code Starter Kit

- [github repository](https://github.ibm.com/cacf-jp-automation/IMaC_startkit)  contains all public code
- [Host list](table.html) shows list of hosts by table style using Tabulator
- [Host list edit](edit.html) enables JSON file edit using JSON Editor



## What is Infrastructure as Code ?

As you know, IaC stands for Infrastructure as Code is a famous word. IaC is expected to build an IT infrastructure with Code automatically. It create a significant benefit on operations of business application. The IMaC extends the concept of Infrastructure as Code. IMaC is trying to manage the existing infrastructure. The legacy old styled Business Application Infrastructure, which cannot be built automatically by IaC, is considered as outside of scope of IaC. But, even though it could not be built by IaC, there are needs to utilize the introduced capability of IaC.

## Concept of IMaC

In case of IMaC, Idempotency is still a most important factor as like IaC. The target value of configuration management code which is represented by a `cmdb.json` will be applied to the target managed systems with IaC styled mechanism and keeping Idempotency.


参考：
「Infrastructure as Codeに疲れたので、僕たちが本来やりたかったことを整理する」を１年掛けて整理した
https://medium.com/@shogomuranushi/infrastructure-as-code%E3%81%AB%E7%96%B2%E3%82%8C%E3%81%9F%E3%81%AE%E3%81%A7-%E5%83%95%E3%81%9F%E3%81%A1%E3%81%8C%E6%9C%AC%E6%9D%A5%E3%82%84%E3%82%8A%E3%81%9F%E3%81%8B%E3%81%A3%E3%81%9F%E3%81%93%E3%81%A8%E3%82%92%E6%95%B4%E7%90%86%E3%81%99%E3%82%8B-%E3%82%92%EF%BC%91%E5%B9%B4%E6%8E%9B%E3%81%91%E3%81%A6%E6%95%B4%E7%90%86%E3%81%97%E3%81%9F-ad435d953471
