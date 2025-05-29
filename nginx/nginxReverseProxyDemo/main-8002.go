package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        // 设置响应头，指定内容类型为HTML
        w.Header().Set("Content-Type", "text/html")
        
        // 使用正确的HTML标签
        fmt.Fprint(w, "<h1>Port 8002!</h1>\n")
    })

    // 启动服务器，监听8002端口
    fmt.Println("服务器启动，访问 http://localhost:8002")
    http.ListenAndServe(":8002", nil)
}