# adidas site tree

Mapped 2026-11-21 with Playwright (headless Chromium) before screenshots. Desktop viewport 1440x900. Phone viewport 390x844. Signed out. No form was submitted.

## Boundary

| Host | What loaded | Decision |
|---|---|---|
| `https://www.adidas.com/` | HTTP 403. Title "adidas". Body is the Akamai Access Denied page ("UNABLE TO GIVE YOU ACCESS TO OUR SITE AT THIS TIME") plus a Reference Error. No storefront rendered. The reference id is not recorded. | Recorded. Not captured. No package invented for this host. |
| `https://www.adidas.com/us` | Same 403 Access Denied page. | Recorded. Not captured. |
| `https://www.adidas.com.cn/` | HTTP 200. Title "阿迪达斯官方旗舰店". Storefront rendered in zh-CN. | This is the captured surface. |

The global site is the known Akamai block. The China flagship is a different front end (prices in CNY, `lib-*` components). Do not treat its tokens as the global storefront.

## Shell

The page is a fixed-height app shell. `document` scroll height stays at the viewport. The scrolling node is `.flex.flex-col` (`overflow: hidden auto`), about 6482px of home content inside a 900px frame on desktop.

A staff dialog (`.lib-dialog`, "请修改初始密码", button "立即修改") mounts on desktop loads, including signed-out sessions. It has no close control. "立即修改" is a password-change action, so it was not clicked. The dialog is a capture obstacle, not a public page. A second dialog, "确认退出员工帐号" (取消 / 确定), stays unmounted (`mobile-only`, zero size). Neither was submitted.

There is no cookie banner and no dark theme control on the captured surfaces.

## Desktop (1440)

Header is two strips, about 124px: a black utility strip, then the nav bar.

| Control | Opens |
|---|---|
| Wordmark (`.logo`) | `/` |
| 在线客服 (`.online`) | No navigation and no panel on this visit. Footer lists the same label next to the published service line. |
| 请登录 (`.loginin`) | Login drawer (`.popover.login-popover`, `.pop-container`). Stops this branch. See Login wall. |
| Profile icon (`.icon-menu_profile_32`) | Same login drawer. Stops this branch. |
| Search pill (`.search-bar-box`, placeholder "温暖三条纹") | Search overlay (`.search-overlay`, about 1440x518) with a text field and hot-search chips (温暖三条纹, 雪境漫游, 山川里, 新品首降, 明星同款, 学生认证享优惠). Chip clicks were not followed (they run a search). The field was not submitted. |
| Bag icon (`.icon-menu_shoppingbag_32`) | `/cart` |
| 男装, 男鞋, 女装, 女鞋, 儿童, 配件 | Meant to open the catalog mega-menu. See Catalog menu. |
| 更多精彩 | Scrolls the nav rail to the second set (返回, 尖货, 运动, 科技, 品牌). The click did not move the rail in this headless session. |
| 返回 | Scrolls the nav rail back to the first set. Same headless miss. |
| 尖货, 运动, 科技, 品牌 | Second-rail catalog labels. Same mega-menu, not opened by the click in this session. |

Promo strip under the header (雪境漫游, 热门搜索, and campaign chips) sits in the header text. Those chips were not clicked.

### Catalog menu

`.catalog-bar` holds one `.catalog-container` with 10 columns and 248 links. Its parent is `display: none` until a catalog label opens it. A real hover and a DOM click on 男装 left that parent hidden in this headless session, so the open menu was not screenshotted. The links are in the DOM. Columns, with the first links:

| Column | First links |
|---|---|
| 运动场景 (men's apparel) | 跑步 `/plp/sp_run_app_male`, 足球 `/plp/sp_football_app_male`, 篮球 `/plp/sp_basketball_app_male`, 训练 `/plp/sp_train_app_male` |
| 热门主推 (men's shoes) | TTOE `/plp/protype_ftw_Ttoe_man`, SUPERSTAR `/plp/franchise_superstar_men`, FORUM `/plp/franchise_forum_men`, ADIZERO `/plp/franchise_adizero_men` |
| 运动场景 (women) | 跑步 `/plp/sp_run_app_female`, 训练 `/plp/sp_train_app_female`, 户外 `/plp/sp_outdoor_app_female` |
| 热门主推 (women's shoes) | TTOE `/plp/protype_ftw_Ttoe_women`, SUPERSTAR `/plp/franchise_superstar_women` |
| 重磅推荐 (kids) | Disney `/plp/collab_DISNEY_kids`, 全部联名 `/plp/catalog_kids_joint_all`, SAMBA `/plp/franchise_samba_kids_8_14` |
| 男子 包袋 | 双肩包 `/plp/prodtype_acc_backpack_male`, 斜挎包 `/plp/prodtype_acc_crossbody_male` |
| 新潮体育运动 | 户外 `/plp/outdoor_all`, 高尔夫 `/plp/golf_all`, 瑜伽 `/plp/yoga`, 网球 `/plp/tennis_all` |

The same tree is public, already open, at `/siteMap` and (on the phone) at `/category`. Captures use those pages plus one representative PLP, not all 248 listing URLs.

### Home body

Campaign and product links, all public:

| Control | Opens |
|---|---|
| Hero banner | `/splp?contentId=SPLP_ncyCqVHY&tabFilter=customized_001164` |
| Hero 立即选购 | Same campaign (button on the banner) |
| Tile row | `/splp?contentId=SPLP_NGuAJiSc`, `/splp?contentId=SPLP_bSqAZSmY`, `/splp?contentId=SPLP_vBTmxFVV`, and a PDP `/pdp?articleId=KH7678` |
| Brand tiles | `/clp?contentId=904`, `/plp/sport_all`, `/plp/brand_SPORTSWEAR`, `/plp/originals_all`, `/plp/brand_TERREX`, `/plp/brand_aSMC`, `/plp/catalog_brand_kids` |
| Gender bands | `/plp/women_all`, `/plp/men_all`, `/plp/kid_all` |
| Product cards | `/pdp?articleId=<sku>` |

Representative pages that loaded (HTTP 200):

| Page | URL | What is on it |
|---|---|---|
| Catalogue | `/plp/sp_run_app_male` | Filter/sort row (综合, 价格, 新品, 性别, 产品分类, 品牌, 运动类型, 服饰类型, 折扣力度, 筛选) and product tiles |
| Campaign listing | `/splp?contentId=SPLP_NGuAJiSc` | Tabs 鞋类 / 服装 / 箱包/附配件, the same filter language, product tiles |
| Product | `/pdp?articleId=JP1477` | Gallery, title, price, 商品评价, 商品详情, 试穿报告. Purchase bar is local UI. Not submitted. |
| Empty bag | `/cart` | "您的购物袋是空的" plus a recommendation row |
| Site map | `/siteMap` | The catalog tree as a page |
| Content page | `/clp?contentId=904` | Brand/content layout, "查看全部" links |
| Account (desktop direct URL) | `/my-account` | Did not open an account shell. Rendered the home campaign. Treated as not signed in. |
| Privacy | `/my-account/privacy-statement` | Policy text plus an account-centre nav (我的积分, 订单中心, 地址簿, 联系我们, 条款与细则, 使用条款, 物流配送规则, 退换货规则, 会员规则, 下单指南). Those account links are a login wall. Not followed. |

### Footer

| Control | Opens |
|---|---|
| 网站地图 | `/siteMap` |
| 隐私声明 | `/my-account/privacy-statement` |
| 客服热线 | `tel:` link to the published service number. Not activated. |
| 关于adidas | `javascript:void(0)`. No navigation. |
| 营业执照 | External image of the published business licence. Not followed. |
| ICP / 公网安备 | External registry sites. Not followed. |
| 微博 去关注 | External Weibo. Not followed. |
| 员工登录 | Login wall. Not followed. |
| 常见问题, 网站政策, 物流配送规则, 退换货规则, 会员规则, 下单指南 | Named in the footer text. The copies that have their own URLs are linked from the privacy page's account nav. Not followed past the login wall. |

### Login wall (branch stops)

Profile icon and 请登录 open `.login-popover`: "欢迎你来adiClub", phone field, 手机号登录/注册, 账号密码登录, 非会员登录. No email was typed. No code was requested. No password was typed. No button in that drawer was clicked. Account, checkout, order, address, and employee-login URLs are the same wall.

## Phone (390)

The desktop category rail is not mounted. A bottom tab bar (`.lib-tab-bar`) is.

| Control | Opens |
|---|---|
| Search pill | Search field (placeholder "温暖三条纹") on `/?VisibleFlag=replace`. Not submitted. |
| 首页 | `/` |
| 分类 | `/category` (the catalog tree, already open: 男装 through 品牌, then 运动场景, 夹克/外套, and the rest) |
| 购物袋 | `/cart` (empty bag, "免费配送") |
| 我的 | `/my-account` phone shell: 登录注册, 我的订单, 待付款, 待收货, 待评价, 退换. Login wall. 登录注册 was not clicked. |

No burger control is mounted at 390. The wordmark is the performance icon at the left of the search pill.

## Not reachable, and why

| Thing | Why it stops |
|---|---|
| `adidas.com` and `adidas.com/us` | 403 before any page renders |
| Signed-in account, orders, addresses, checkout, employee login | Login or signup wall |
| Staff password dialog action | Password change. Not clicked. |
| Search submit, newsletter, survey, onboarding | Forms. Not submitted. |
| Catalog mega-menu open state | Parent stays `display: none` after hover and click in this headless session. The same links are on `/siteMap` and `/category`. |
| Dark theme | No theme control on the captured surfaces |
| Every one of the 248 PLP URLs | Same listing template. One PLP, one campaign listing, the site map, and the category page stand for the set. |
