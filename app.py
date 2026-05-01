import streamlit as st
import time
import random

st.set_page_config(page_title="AI设计团队系统", layout="wide")

st.title("🧠 AI设计团队操作系统 Demo")

product = st.text_input("输入产品", "高端不锈钢厨具")

def fake_logs():
    return [
        "初始化Agent系统...",
        "加载模型参数...",
        "创意Agent生成方向中...",
        "生成3个创意方案",
        "设计Agent执行中...",
        "调用视觉生成模块...",
        "策略Agent优化中...",
        "数据Agent评分中...",
        "执行多轮博弈...",
        "收敛最优解..."
    ]

def run_system(product):
    ideas = [
        f"{product}｜极简高端风",
        f"{product}｜工业质感风",
        f"{product}｜生活方式场景"
    ]

    results = []
    for idea in ideas:
        score = round(random.uniform(0.65, 0.95), 2)
        results.append({"idea": idea, "score": score})

    best = sorted(results, key=lambda x: x["score"], reverse=True)[0]
    return best, results


if st.button("🚀 启动多Agent协作"):

    col1, col2 = st.columns([2, 1])

    with col2:
        st.subheader("📡 系统日志")
        log_box = st.empty()

    with col1:
        st.subheader("🧩 Agent执行过程")
        progress = st.progress(0)

        logs = fake_logs()

        for i, log in enumerate(logs):
            log_box.text(log)
            progress.progress((i + 1) / len(logs))
            time.sleep(0.4)

        best, results = run_system(product)

        st.success("✅ 任务完成")

        st.subheader("📊 全部方案")
        for r in results:
            st.write(f"{r['idea']} ｜ 评分：{r['score']}")

        st.subheader("🏆 最优方案")
        st.metric("最佳创意", best["idea"])
        st.metric("预测点击率", f"{int(best['score']*100)}%")

st.sidebar.success("系统运行正常")
st.sidebar.metric("Token消耗", "2.3M")
st.sidebar.metric("系统效率提升", "4x")
