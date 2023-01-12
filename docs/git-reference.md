# common git commands

## remove all local branches except master

<https://coderwall.com/p/x3jmig/remove-all-your-local-git-branches-but-keep-master>

```bash
git branch | grep -v "master" | xargs git branch -D
```
