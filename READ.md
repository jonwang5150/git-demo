# GIT指令

### 查詢版本號
- git --version


### 建立基本資訊
- git config --global user.name {name}
- git config --global user.email {email}


### 查找config
- git config --list


### 建立倉庫
- git init


### 觀察狀態
- git status(untrack,added,modified,deleted)


### 加入暫存區
- git add filename
	- git add . (加入所有)


### 觀察object編碼
- git cat-file -p sha1(content)
	- 內容

- git cat-file -t sha1(type)
	- 型態

- git cat-file -s sha1(size)
	- 大小

### 觀察暫存區的檔案
- git ls-files
	-s

### 將暫存區的檔案加入倉庫
- git commit -m "message"
- git commit -am "demo"
	- 不想增加新的commit紀錄
		- git commit --amend(按insert鍵增加修正內容>>>esc:wq)



### 查看目前commit狀態
- git log
	- --git log --oneline

### 刪除恢復
- git restore


### 指令刪除
- git rm -f filename(手動刪除+git add)
	--- git restore --staged filename(恢復,要兩動)


### 將檔案搬離暫存/倉庫區
- git rm --cached filename


### 分支指令
- git branch

### 新增分支
- git branch branch-name


### 切換分支
- git checkout branch-name

- git checkout -b test2
	- 新增branch+checkout

### 更改分支名稱
- git branch -m dev test2

### 刪除分支(要切換到別的分支如master)
- git branch -D
	- 
### 合併分支
- git checkout master
	- git merge test

### 衝突處理
- 確認修改狀態

### 切換commit
- git checkout commit-object(git log裡看)

### 觀看目前commit歷程
- git reflog


### 恢復commit指令
- git reset
	- mixed
	-- soft
	-- hard

### 綁定github網址
- git remote add origin https://github.com/jonwang5150/git-demo


### 上傳程式碼
- git push -u origin master(第一次)
	- git push(之後修改)