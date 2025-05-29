'''
向本地服务器（http://127.0.0.1:5000/bili）发送了一个 POST 请求，
携带了一个包含 ordered_string 的 JSON 数据。服务器返回了一个 JSON 响应，包含 sign 和 status 字段
'''
import requests

res = requests.post(
    url="http://127.0.0.1:5000/bili",
    json={
        "ordered_string": "actual_played_time=0&aid=851776257&appkey=1d8b6e7d45233436&auto_play=0&build=6240300&c_locale=zh_CN&channel=xx1_gdt_wm_253&cid=516350598&epid=0&epid_status=&from=6&from_spmid=tm.recommend.0.0&last_play_progress_time=0&list_play_time=0&max_play_progress_time=0&mid=0&miniplayer_play_time=0&mobi_app=android&network_type=1&paused_time=0&platform=android&play_status=0&play_type=1&played_time=0&quality=80&s_locale=zh_CN&session=897a6991b1f7489f915e420c9b82136d9c5dec62&sid=0&spmid=main.ugc-video-detail_vertical.0.0&start_ts=0&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%2226.24.0%22%2C%22abtest%22%3A%22%22%7D&sub_type=0&total_time=0&ts=1655220112&type=3&user_status=0&video_duration=232"
    }
)

print(res.json())
#{'sign': '9fa0a3a8e46f51548987979309ab6cdb', 'status': True}
