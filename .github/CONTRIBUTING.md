# Contributing

TODO: the guidelines to be updated for LAI DevRel community

Welcome to the Lightning AI Dev community! We're building the most advanced research platform on the planet to implement the latest, best practices
and integrations that the amazing PyTorch team and other research organization rolls out!

If you are new to open source, check out [this blog to get started with your first Open Source contribution](https://devblog.pytorchlightning.ai/quick-contribution-guide-86d977171b3a).

## Main Core Value: One less thing to remember

Simplify the API as much as possible from the user perspective.
Any additions or improvements should minimize the things the user needs to remember.

For example: One benefit of the `validation_step` is that the user doesn't have to remember to set the model to .eval().
This helps users avoid all sorts of subtle errors.

## Lightning Design Principles

We encourage all sorts of contributions you're interested in adding! When coding for Lightning, please follow these principles.

### No PyTorch Interference

We don't want to add any abstractions on top of pure PyTorch.
This gives researchers all the control they need without having to learn yet another framework.

### Simple Internal Code

It's useful for users to look at the code and understand very quickly what's happening.
Many users won't be engineers. Thus we need to value clear, simple code over condensed ninja moves.
While that's super cool, this isn't the project for that :)

### Force User Decisions To Best Practices

There are 1,000 ways to do something. However, eventually one popular solution becomes standard practice, and everyone follows.
We try to find the best way to solve a particular problem, and then force our users to use it for readability and simplicity.
A good example is accumulated gradients.
There are many different ways to implement it, we just pick one and force users to use it.
A bad forced decision would be to make users use a specific library to do something.

When something becomes a best practice, we add it to the framework. This is usually something like bits of code in utils or in the model file that everyone keeps adding over and over again across projects. When this happens, bring that code inside the trainer and add a flag for it.

### Simple External API

What makes sense to you may not make sense to others. When creating an issue with an API change suggestion, please validate that it makes sense for others.
Treat code changes the way you treat a startup: validate that it's a needed feature, then add if it makes sense for many people.

### Backward-compatible API

We all hate updating our deep learning packages because we don't want to refactor a bunch of stuff. In Lightning, we make sure every change we make which could break an API is backward compatible with good deprecation warnings.

**You shouldn't be afraid to upgrade Lightning :)**

### Gain User Trust

As a researcher, you can't have any part of your code going wrong. So, make thorough tests to ensure that every implementation of a new trick or subtle change is correct.

### Interoperability

Have a favorite feature from other libraries like fast.ai or transformers? Those should just work with lightning as well. Grab your favorite model or learning rate scheduler from your favorite library and run it in Lightning.

## Guidelines

### Developments scripts

To build the documentation locally, simply execute the following commands from project root (only for Unix):

- `make clean` cleans repo from temp/generated files
- `make docs` builds documentation under _docs/build/html_
- `make test` runs all project's tests with coverage

### Original code

All added or edited code shall be the own original work of the particular contributor.
If you use some third-party implementation, all such blocks/functions/modules shall be properly referred and if possible also agreed by code's author. For example - `This code is inspired from http://...`.
In case you adding new dependencies, make sure that they are compatible with the actual PyTorch Lightning license (ie. dependencies should be _at least_ as permissive as the PyTorch Lightning license).

### Coding Style

1. Use f-strings for output formation (except logging when we stay with lazy `logging.info("Hello %s!", name)`.
1. You can use [pre-commit](https://pre-commit.com/) to make sure your code style is correct.

### Documentation

To learn about development of docs, check out the docs [README.md](https://github.com/Lightning-AI/lightning/blob/master/docs/README.md).

### Testing

To learn about tests, check out the tests [README.md](https://github.com/Lightning-AI/lightning/blob/master/tests/README.md).

### Pull Request

We welcome any useful contribution! For your convenience here's a recommended workflow:

1. Think about what you want to do - fix a bug, repair docs, etc. If you want to implement a new feature or enhance an existing one.

   - Start by opening a GitHub issue to explain the feature and the motivation.
     In the case of features, ask yourself first - Is this NECESSARY for Lightning? There are some PRs that are just
     purely about adding engineering complexity which has no place in Lightning.
   - Core contributors will take a look (it might take some time - we are often overloaded with issues!) and discuss it.
   - Once an agreement was reached - start coding.

1. Start your work locally.

   - Create a branch and prepare your changes.
   - Tip: do not work on your master branch directly, it may become complicated when you need to rebase.
   - Tip: give your PR a good name! It will be useful later when you may work on multiple tasks/PRs.

1. Test your code!

   - It is always good practice to start coding by creating a test case, verifying it breaks with current behaviour, and passes with your new changes.
   - Make sure your new tests cover all different edge cases.
   - Make sure all exceptions raised are tested.
   - Make sure all warnings raised are tested.

1. If your PR is not ready for reviews, but you want to run it on our CI, open a "Draft PR" to let us know you don't need feedback yet.

1. If any of the existing tests fail in your PR on our CI, refer to the following READMEs to identify what's failing and try to address it.

   - [Test README](https://github.com/Lightning-AI/lightning/blob/master/tests/README.md)
   - [CI/CD README](https://github.com/Lightning-AI/lightning/blob/master/.github/workflows/README.md)

1. When you feel ready for integrating your work, mark your PR "Ready for review".

   - Your code should be readable and follow the project's design principles.
   - Make sure all tests are passing and any new code is tested for (coverage!).
   - Make sure you link the GitHub issue to your PR.
   - Make sure any docs for that piece of code are updated, or added.
   - The code should be elegant and simple. No over-engineering or hard-to-read code.

   Do your best but don't sweat about perfection! We do code-review to find any missed items.
   If you need help, don't hesitate to ping the core team on the PR.

1. Use tags in PR name for the following cases:

   - **\[blocked by #<number>\]** if your work is dependent on other PRs.
   - **\[wip\]** when you start to re-edit your work, mark it so no one will accidentally merge it in meantime.
