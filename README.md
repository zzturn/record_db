# record_db

本仓库将 Github Issues 作为数据库，进行网页收藏。

**出发点：**

目前各个稍后读、网页剪藏等 APP 均以各自服务器为数据中心，迁移成本较大，且后期能否持续维护存疑。

而 Github 对程序员来说天然友好，虽然也有着自己的服务器，但相比市面其它的 APP，个人认为其更具稳定性、持久性。People Die, but Long Live GitHub. 

此外，Github 提供了完善的 API 接口，十分方便数据迁移，灵活性较高。

**未来构想：**

- 将 Github 作为个人知识库，并提供 API 以便在移动端、web 端搜索。比如，在使用 Google 时，可以编写油猴脚本/浏览器插件使得同步显示在个人知识库里的搜索结果。

- 将 Github 作为日常记录数据库，记录自己平时的行为习惯，用于日后分析，或许会发现新的自己。



**基本概念介绍：**

一个 Github Issues 里包含， `title`, `body`, `comments`, `labels`, `milestone` 等等

其中 Issue 与 `title`, `body`, `milestone` 均为一对多关系，与 `comments`, `labels` 为一对多关系。

那么我们可以有如下映射关系

| 字段名      | 用途           | 例子                                                         |
| ----------- | -------------- | ------------------------------------------------------------ |
| `title`     | 文章标题       | Github Actions Variables - GitHub Docs                       |
| `body`      | 网页链接       | https://docs.github.com/en/actions/learn-github-actions/variables |
| `comments`  | 补充说明，备注 | 关于 Github Actions 变量的文档，方便后续查阅                 |
| `milestone` | 分类           | 文档                                                         |
| `labels`    | 标签           | GitHub, workflow                                             |


对于一个想要收藏的链接来说，基本可以包含了所有必要的信息了，如果还需要其它信息，可以接着在 comments 里添加。


**其它：**

在 Github Issues 有改动时，GitHub Actions 都会重新生成 [record.md](https://raw.githubusercontent.com/luoxin971/record_db/master/record.md) 文件，再根据 md 文件使用 pandoc 转换成 html 文件，托管于 [Github Pages](https://blog.luoxin.vip/record_db)


**TODO：**

| 需求                                                     | 优先级 | 难度  |
| -------------------------------------------------------- | ------ | ----- |
| 编写 Chrome 插件/油猴脚本实现一键收藏                    | ★★★★★  | ★★★☆☆ |
| 调研在微信端实现快速收藏的方法                           | ★★★★★  | ★★★★☆ |
| 调研在 IOS 系统内快速收藏的方法                          | ★★★★★  | ★★★★☆ |
| 优化生成的静态网页样式                                  | ★★★★☆ | ★★★☆☆ |
| 增加链接剪藏功能，收到后自动剪藏整个内容放在 comments 中 | ★★★★☆  | ★★★★★ |
| 添加全文搜索接口，便于系统性查询                         | ★★★☆☆  | ★★★★★ |
| 编写 Chrome 插件/油猴脚本实现在搜索引擎内同步搜索        | ★★★☆☆  | ★★★★☆ |

