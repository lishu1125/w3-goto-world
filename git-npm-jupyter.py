### git

'''git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/hoochanlon/private.git //远程链接
git push -u origin master

git checkout gh-pages //切换分支
git checkout -b gh-pages //创建并切换分支
git push origin branch-name //直接push 到repo的相关分支

git branch -r -d origin/branch-name //删除分支
git push origin :branch-name //删除远程分支
git rm -r --cached mydir  //删除mydir文件夹，-n 即为展示不删除

git fetch --all //指令是下载远程仓库最新内容，不做合并
git reset --hard origin/master  //指令把HEAD指向master最新版本
git pull //强行合并
git fetch //下载远程仓库内容/（不同的下载，相同的留下）兼容
git merge //合并


git remote set-url origin repo.git //修改远程仓库地址

### npm

npm login
npm pulish
npm unpublish pkg --force

[npm增删改](https://segmentfault.com/a/1190000017479985)

### jupyter

* [jupyter安装及目录生成](https://www.cnblogs.com/jayafsmw/p/12286580.html)
* [那些在线的Jupyter](https://blog.csdn.net/hxpjava1/article/details/86763331)

pip国内镜像

* http://mirrors.aliyun.com/pypi/simple/
* https://pypi.mirrors.ustc.edu.cn/simple/
* http://pypi.douban.com/simple/
* https://pypi.tuna.tsinghua.edu.cn/simple/
* http://pypi.mirrors.ustc.edu.cn/simple/

example：

`pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple`

`pip3 install jupyter -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com`'''
