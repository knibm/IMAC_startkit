<!-- This should be the location of the title of the repository, normally the short name -->
# IMaC_startkit
Infrastructure Management as Code Starter Kit

<!-- Build Status, is a great thing to have at the top of your repository, it shows that you take your CI/CD as first class citizens -->
[![Build Status](https://travis.ibm.com/cacf-jp-automation/IMaC_startkit.svg?token=2yTtXAokpWkqEud8ssW5&branch=master)](https://travis.ibm.com/cacf-jp-automation/IMaC_startkit)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

<!-- Not always needed, but a scope helps the user understand in a short sentance like below, why this repo exists -->
## Scope

This repository provide a simple and reusable implementation of 'Infrastructure Management as Code' as sample code.

### What is Infrastructure as Code ?

IaC stands for 'Infrastructure as Code' is a famous word and introduced a new way to IT operations. IaC is expected to build an IT infrastructure with Code automatically. It create a significant benefit on operations of business application. The IMaC extends the concept of Infrastructure as Code. IMaC is trying to manage the existing infrastructure. The legacy old styled Business Application Infrastructure, which cannot be built automatically by IaC, is considered as outside of scope of IaC. But, even though it could not be built by IaC, there are needs to utilize the introduced capability of IaC.

### Concept of IMaC

In case of IMaC, Idempotency is still a most important factor as like IaC. The target value of configuration management code which is represented by a `cmdb.json`. The values on `cmdb.json` will be applied to the target managed systems with IaC styled mechanism and keeping Idempotency.


<!-- A more detailed Usage or detailed explaination of the repository here -->
## Usage

This repository contains some example best practices for open source repositories:

* [LICENSE](LICENSE)
* [README.md](README.md)
* [CONTRIBUTING.md](CONTRIBUTING.md)
* [MAINTAINERS.md](MAINTAINERS.md)
<!-- A Changelog allows you to track major changes and things that happen, https://github.com/github-changelog-generator/github-changelog-generator can help automate the process -->

> These are optional

<!-- The following are OPTIONAL, but strongly suggested to have in your repository. -->
* [Example View](https://pages.github.ibm.com/cacf-jp-automation/IMaC_startkit/) - You can see user page https://pages.github.ibm.com/cacf-jp-automation/IMaC_startkit/ .
* [travis.yml](.travis.yml) - This is a example `.travis.yml`, please take a look https://docs.travis-ci.com/user/tutorial/ for more details.


<!-- A notes section is useful for anything that isn't covered in the Usage or Scope. Like what we have below. -->
## Notes

<!-- Questions can be useful but optional, this gives you a place to say, "This is how to contact this project maintainers or create PRs -->
If you have any questions or issues you can create a new [issue here][issues].

Pull requests are very welcome! Make sure your patches are well tested.
Ideally create a topic branch for every separate change you make. For
example:

1. Fork the repo
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## License

All source files must include a Copyright and License header. The SPDX license header is 
preferred because it can be easily scanned.

If you would like to see the detailed LICENSE click [here](LICENSE).

```text
#
# Copyright 2020- IBM Inc. All rights reserved
# SPDX-License-Identifier: Apache2.0
#
```
## Authors

Please check GitHub list of contributors.

[issues]: https://github.com/IBM/repo-template/issues/new
