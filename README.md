[![PyPI](https://img.shields.io/pypi/v/powerline-travis-ci?color=blue&logo=python&logoColor=green&style=plastic)](https://pypi.org/project/powerline-travis-ci/)
[![Downloads](http://pepy.tech/badge/powerline-travis-ci)](http://pepy.tech/count/powerline-travis-ci)

# powerline-travis-ci

A light-hearted [Powerline](https://github.com/powerline/powerline) segment for fetching and showing the status
of the last build on travis. The segment will only be shown if the current directory contains a `.travis.yml` file.

**Keep in mind that powerline-travis-ci is in early, rapid development stage so its API/configuration format may change.**

- [Requirements](#requirements)
- [Installation](#installation)
- [Activation](#activation)
- [Configuration and Customization](#configuration-and-customization)
- [Examples](#examples)
- [Changelog](#changelog)

## Requirements

 - [Powerline](https://github.com/powerline/powerline)
 - A [travis-ci.com](https://travis-ci.com) API token
 
## Installation
 
```
pip install powerline-travis-ci
```

## Activation
 
The very minimum required to activate the segment is to add the following to your theme JSON:
 
```json
{
   "function": "powerline_travis_ci.latest_build_state",
   "args": {
        "token": API_TOKEN,
        "username": TRAVIS_USERNAME
    }
}
```
 
and the following to your colorscheme JSON (the colors can be customized):
 
```json
"groups": {
      "latest_travis_build_state": {
          "fg": "gray9",
          "bg": "gray2",
          "attrs": []
    }
}
```
 
## Configuration and Customization
 
The following optional `args` are available:
  
| Argument | Type | Description | Default
| --- | --- | --- | --- |
| `canceled_text` | string | Text or icon to show for the `canceled` state | `"Canceled"` |
| `created_text` | string | Text or icon to show for the `created` state | `"Created"` |
| `errored_text` | string | Text or icon to show for the `errored` state | `"Errored"` | 
| `failed_text` | string | Text or icon to show for the `failed` state | `"Failed"` |
| `for_current_branch` | boolean | If `true` the state shown is the state of the latest build of the checked out git branch | `false` |
| `git_path` | string | Only used if `for_current_branch` is `true` | `"git"` |
| `passed_text` | string | Text or icon to show for the `passed` state | `"Passed"` |
| `post_state_text` | string | Text or icon to append the state.<br>If contains `<travis_url>` a clickable link to travis will be shown (if the supported by your terminal) | `""` |
| `pre_state_text` | string | Text or icon to prepend before the state.<br>If contains `<travis_url>` a clickable link to travis will be shown (if the supported by your terminal) | `""` |
| `received_text` | string | Text or icon to show for the `received` state | `"Received"` |
| `show_state_branch` | boolean | If `true` the name of the git branch will be shown along the state | `false` |
| `started_text` | string | Text or icon to show for the `started` state | `"Started"` |

### Highlight Groups

In addition to the generic `latest_travis_build_state` group, each state can be customized independently with highlight group `latest_travis_build_state_{state}`.

For example,

```json
"latest_travis_build_state_passed": {
    "fg": "white",
    "bg": "darkestgreen",
    "attrs": []
}
```

If a specific state does not have a highlight group then the style of `"latest_travis_build_state"` group will be used.

## Examples

##### Default configuration

![default](readme-images/default.png?raw=true)
  
##### Customized text and highlight groups for "passed" and "failed" states

```json
{
  "function": "powerline_travis_ci.latest_build_state",
  "args": {
      "token": API_TOKEN,
      "username": TRAVIS_USERNAME,
      "passed_text": "✔",
      "failed_text": "❌",
      "pre_state_text": "Travis: "
  }
}
```
  
```json
"latest_travis_build_state": {
  "fg": "white",
  "bg": "gray2",
  "attrs": []
},
"latest_travis_build_state_passed": {
  "fg": "white",
  "bg": "darkestgreen",
  "attrs": []
},
"latest_travis_build_state_failed": {
  "fg": "white",
  "bg": "darkestred",
  "attrs": []
}
```
  
![customized-passed](readme-images/customized-passed.png?raw=true)
  
![customized-faild](readme-images/customized-failed.png?raw=true)

## Changelog

### 0.1 - Nov. 6 2020
Initial release
