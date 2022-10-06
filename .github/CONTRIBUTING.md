# Contributing Guidelines

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

Welcome to the Lightning AI Dev community!

Lightning AI is the first operatings system for AI. Build state-of-the art models with Lightning Trainer and use them inside Lightning Apps (end-to-end ML systems).

![](/assets/ecosystem.png)

These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

We welcome any kind of contribution to our software, from simple comment or question to a full fledged pull request. Please read and follow our [Code of Conduct](./CODE_OF_CONDUCT.md).

A contribution can be one of the following cases:

1. you have a question;
1. you want to write content around the Lightning Ecosystem;
1. you want to do evangelism for Lightning AI;
1. you think you may have found a bug (including unexpected behavior);
1. you want to make some kind of change to the code base (e.g. to fix a bug, to add a new feature, to update documentation);
1. you want to make a new release of the code base.

If you are new to open source, check out [this blog to get started with your first Open Source contribution](https://devblog.pytorchlightning.ai/quick-contribution-guide-86d977171b3a).

## You have a question
1. Use the search functionality here to see if someone already filed the same issue or check out Docs.
1. If your issue search did not yield any relevant results, make a new issue.
1. Apply the "Question" label; apply other labels when relevant.
1. You can join our [Slack group](https://join.slack.com/t/pytorch-lightning/shared_invite/zt-1dm4phlc0-84Jv9_8Mp_tWraICOJ467Q) as well.


## Guidelines

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
