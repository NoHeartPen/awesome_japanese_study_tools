
/*
该脚本基于[Auto.js](https://pro.autojs.org/)开发，用于在每次解锁手机后生成一个弹窗提醒自己有多少单词需要整理，拖延症必备:)
*/

auto.waitFor();
auto.setMode("normal");
setScreenMetrics(1080,2340)
console.setSize(500,500)
console.setPosition(500,800)

var r = http.get("https://api.frdic.com/api/open/v1/studylist/words/0?language=en&category_id=0", {
    headers: {
    'Authorization': '请到 https://my.eudic.net/OpenAPI/Authorization 获取APIKey'
    }
    });
    
//log(r.statusCode);//用于判断错误原因
    
wordlist = r.body.string()
wordnumber = wordlist.split('\{"word"\:"').length-2

console.show()
log("有"+wordnumber+"个单词待处理")