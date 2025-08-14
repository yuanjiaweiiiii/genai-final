import streamlit as st
import time
import requests

# 页面配置
st.set_page_config(page_title="MSADS Chatbot", layout="centered")

# Logo 和标题
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/University_of_Chicago_wordmark.svg/2560px-University_of_Chicago_wordmark.svg.png",
    width=350
)
st.markdown("<h1 style='text-align: center;'>🎓📚 Welcome to the <span style='color:#800000;'>UChicago</span> MSADS Q&A Bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask anything about the program: <strong>admissions, curriculum, faculty, careers…</strong></p>", unsafe_allow_html=True)
st.markdown("---")

# 初始化 session state
if "history" not in st.session_state:
    st.session_state.history = []

# 清空按钮
if st.button("🧹 Clear Conversation"):
    st.session_state.history = []

# 用户输入
user_question = st.text_input("💬 Ask a question about the MSADS program:")

# 回答处理逻辑
if user_question:
    with st.spinner("🤖 Thinking..."):
        time.sleep(1.2)

        # ✅ 替换为你真实的 API 地址
        try:
            response = requests.post(
                "http://localhost:5000/ask",  # <-- 替换成你们组的实际后端接口
                json={"question": user_question},
                timeout=10
            )
            response.raise_for_status()
            result = response.json()

            answer = result.get("answer", "No answer received.")
            citations = result.get("citations", [])

        except Exception as e:
            answer = f"⚠️ Error from API: {e}"
            citations = []

    # 显示当前回答
    st.markdown("### ✅ Answer")
    st.success(answer)

    if citations:
        st.markdown("**🔗 Source(s):**")
        for url in citations:
            st.markdown(f"- [📎 {url}]({url})")

    # 保存到历史记录
    st.session_state.history.append({
        "question": user_question,
        "answer": answer,
        "citations": citations
    })

# 多轮对话历史显示
if st.session_state.history:
    st.markdown("---")
    st.markdown("### 🧾 Previous Q&A")

    for i, qa in enumerate(reversed(st.session_state.history[-5:])):
        with st.expander(f"📌 Q{i+1}: {qa['question']}"):
            st.markdown(f"**Answer:** {qa['answer']}")
            for url in qa['citations']:
                st.markdown(f"- [📎 {url}]({url})")
