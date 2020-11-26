# IMaC_startkit
Infrastructure Management as Code Starter Kit

- [github repository](https://github.com/knibm/IMaC_startkit)  contains all public code
- [Travis CI](https://travis-ci.org/github/knibm/IMaC_startkit) validate the changes
- [Host list](table.html) shows list of hosts by table style using Tabulator
- [Host list edit](edit.html) enables JSON file edit using JSON Editor



## What is Infrastructure as Code ?

As you know, IaC stands for Infrastructure as Code is a famous word. IaC is expected to build an IT infrastructure with Code automatically. It create a significant benefit on operations of business application. The IMaC extends the concept of Infrastructure as Code. IMaC is trying to manage the existing infrastructure. The legacy old styled Business Application Infrastructure, which cannot be built automatically by IaC, is considered as outside of scope of IaC. But, even though it could not be built by IaC, there are needs to utilize the introduced capability of IaC.

## Concept of IMaC

In case of IMaC, Idempotency is still a most important factor as like IaC. The target value of configuration management code which is represented by a `cmdb.json` will be applied to the target managed systems with IaC styled mechanism and keeping Idempotency.
