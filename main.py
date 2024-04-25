import streamlit as st
import openai
import pickle
import os
import time
import json
from streamlit import session_state 
from dotenv import load_dotenv
from openai import OpenAI


# 在使用API密钥和基础URL之前加载.env文件
load_dotenv()

# 现在可以通过os.environ访问这些值
API_BASE = os.environ.get("API_BASE")
API_KEY = os.environ.get("API_KEY")
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=API_KEY,
    base_url=API_BASE
)
os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ["https_proxy"] = "http://127.0.0.1:7890"
#streamlit run dataset.py --server.port 2323
st.set_page_config(
    page_title='基于youtube视频（计划支持bilibili等其他平台）和零一万物大模型构建大语言模型高质量训练数据集（计划支持可自定义输出的训练数据格式）',
    layout="wide",
    page_icon=':robot:',
    initial_sidebar_state="expanded",#“auto”或“expanded”或“collapsed”
         menu_items={
         'Get Help': None,
         'Report a bug': None,
         'About': None
     }
)
# 加载问题库
def load_questions(file_path):
    if not os.path.exists(file_path):
        st.error(f"文件 {file_path} 不存在")
        print(f"文件 {file_path} 不存在")
        return []
    else:
        with open(file_path, "r",encoding='utf-8') as file:
            questions = file.readlines()
        return list(set([q.strip() for q in questions if q !='' and q!='\n']))#去重

# 保存问题库
def save_questions(file_path, questions):
    with open(file_path, "w",encoding='utf-8') as file:
        for question in questions:
            file.write(question + "\n")

# 保存回答
def generate_answer(prompt):
    answer='114514'
    return answer

def save_answers(temp_answers,just_read=False):
    if just_read:
        if os.path.exists("data.pkl"):
            with open("data.pkl", "rb") as file:
                answers = pickle.load(file)
        else:
            answers = {}
        session_state.all_answers=answers
        return True
    else:
        if os.path.exists("lock"):
            return False
        with open("lock", "w") as lock_file:
            lock_file.write("")
        if os.path.exists("data.pkl"):
            with open("data.pkl", "rb") as file:
                answers = pickle.load(file)
        else:
            answers = {}
        answers.update(temp_answers)#覆盖式更新
        
        with open("data.pkl", "wb") as file:
            pickle.dump(answers, file)
        if os.path.exists("lock"):
            os.remove("lock")
        session_state.all_answers=answers
        return True
def save_answers_as_json(answers, file_path):
    data = []
    #print("answers",answers)
    if 0:
        for question, answer in answers.items():#根据情况修改输出格式
            item = {
                "instruction": question,
                "input": "",
                "output": answer
            }
            data.append(item)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    else:
        with open(file_path, "w", encoding="utf-8") as file:
            for question, answer in answers.items(): 
                item = { "prompt": "问题：" + question + "\n", "completion": answer } 
            
                file.write(json.dumps(item, ensure_ascii=False) + "\n")
def reset_text_area():
    if session_state.text_area_tittle=="回答：(内容为空则不保存此回答)":
        session_state.text_area_tittle="回答：(内容为空则不保存此回答) "
    elif session_state.text_area_tittle=="回答：(内容为空则不保存此回答) ":
        session_state.text_area_tittle="回答：(内容为空则不保存此回答)"
def main():
    st.markdown("[公众号：正经人王同学](https://mp.weixin.qq.com/s/_ea6g0pzzeO4WyYtuWycWQ)")
    st.markdown("[本项目开源在github](https://github.com/zjrwtx/VideoQA_databuilder)")
    st.markdown("微信联系我：agi_isallyouneed")
    st.title("VideoQA_databuilder")
    st.markdown("功能描述:基于youtube视频（计划支持bilibili等其他平台）和零一万物大模型构建大语言模型高质量训练数据集（计划支持可自定义输出的训练数据格式）")
    
    st.markdown("使用指南：使用youtubequestion项目生成指定视频的questions文件——本项目读取questions文件——然后基于零一万物模型生成基于视频内容的回答后自我调整——最后将回答保存到answers.json文件。")
    
    API_KEY=st.sidebar.text_input("请填写你的零一万物模型apikey", value='',type="password")
    PROMPT=st.sidebar.text_input("提示词prompt", value= "请给出以下问题的答案：")
    if 'temp_answers' not in session_state:
        session_state.temp_answers={}
    if 'all_answers' not in session_state:
        save_answers(session_state.temp_answers,just_read=True)
        session_state.question_txt="questions.txt"
        session_state.answers_json="answers.json"
        session_state.generated_answer=""
        session_state.text_area_tittle="回答：(内容为空则不保存此回答)"
        session_state.selected_id=0
    session_state.question_txt=st.sidebar.text_input("存有每一条问题的txt", value=session_state.question_txt)
    session_state.answers_json=st.sidebar.text_input("保存回答的json路径", value=session_state.answers_json)
    if 'questions' not in session_state:
        session_state.questions = load_questions(session_state.question_txt)
    selected_questions={}
    for q in range(len(session_state.questions)):
        selected_questions[session_state.questions[q]]=q 
    selectbox_empty = st.empty()
    selected_question = selectbox_empty.selectbox("请选择一个问题：", session_state.questions,index=session_state.selected_id)
    if selected_question:
        session_state.selected_id = selected_questions[selected_question]
        selected_question = selectbox_empty.selectbox("请选择一个问题： ", session_state.questions,index=session_state.selected_id)
        prompt = PROMPT + selected_question
        st.sidebar.write({'预览':prompt})
        user_answer_empty = st.empty()
        user_answer = user_answer_empty.text_area(session_state.text_area_tittle, session_state.generated_answer, height=200)


        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            if st.button("保存全部回答") or len(session_state.temp_answers) >= 10:
                session_state.selected_id=0
                for question in session_state.temp_answers:#删除已经回答的问题，但可以覆盖data.pkl存过的问题
                    session_state.questions.remove(question)
                save_questions(session_state.question_txt, session_state.questions)
                if save_answers(session_state.temp_answers):
                    st.success("全部回答已保存。")
                    session_state.temp_answers = {}
                else:
                    st.error("保存失败，请稍后重试。经常出现此问题是因为死锁，请删除data.pkl文件后重试。")
                    time.sleep(5)
                st.rerun()
        with col2:
            if st.button("零一万物模型生成回答"):
                session_state.generated_answer=''
                try:
                    # 打开文件
                    with open('srt.txt', 'r', encoding='utf-8') as file:
                        # 读取文件内容
                        srt_content = file.read()
                    completion = client.chat.completions.create(
                                    model="yi-34b-chat-0205",
                                    messages=[
                                        {"role": "system", "content": "请你根据"+srt_content+"的内容，详细回答用户的问题。"},
                                        {"role": "user", "content": prompt}
                                        ],
                                    stream=True,
                                )
                    event_count=0
                   
                    for chunk in completion:
                        if chunk.choices[0].delta.content is None:
                            continue
                        # print(chunk.choices[0].delta.content or "", end="", flush=True)
                        outputtext=chunk.choices[0].delta.content
                        
                        print(outputtext)
                        session_state.generated_answer+=outputtext
                        if event_count>10:
                            event_count=0
                            reset_text_area()
                            user_answer = user_answer_empty.text_area(session_state.text_area_tittle, session_state.generated_answer, height=200)
                        event_count+=1
                    reset_text_area()
                    user_answer = user_answer_empty.text_area(session_state.text_area_tittle, session_state.generated_answer, height=200)
                    #st.rerun()
                except Exception as e:
                    print(e)
                    st.error("生成失败，请稍后重试。")
        with col3:
            if st.button("确认此回答(自动下一个)"):
                session_state.generated_answer=''
                if user_answer != '':
                    session_state.temp_answers[selected_question] = user_answer
                elif selected_question in session_state.temp_answers:#内容为空则不保存此回答
                    del session_state.temp_answers[selected_question]#data.pkl存过的问题不清空
                reset_text_area()
                user_answer = user_answer_empty.text_area(session_state.text_area_tittle, height=200)
                session_state.selected_id+=1
                if session_state.selected_id>=len(session_state.questions):
                    session_state.selected_id=0
                st.rerun()
        with col4:
            if st.button("上一个问题"):
                session_state.generated_answer=''
                session_state.selected_id-=1
                if session_state.selected_id<0:
                    session_state.selected_id=len(session_state.questions)-1
                reset_text_area()
                user_answer = user_answer_empty.text_area(session_state.text_area_tittle, height=200)
                st.rerun()
        with col5:
            if st.button("下一个问题"):
                session_state.generated_answer=''
                session_state.selected_id+=1
                if session_state.selected_id>=len(session_state.questions):
                    session_state.selected_id=0
                reset_text_area()
                user_answer = user_answer_empty.text_area(session_state.text_area_tittle, height=200)
                st.rerun()
    if st.sidebar.button("读取该您的questions文件"):
        session_state.selected_id=0
        save_answers(session_state.temp_answers,just_read=True)
        session_state.questions = load_questions(session_state.question_txt)
        st.rerun()
    if st.sidebar.button("导出已保存回答为 JSON文件"):
        save_answers_as_json(session_state.all_answers, session_state.answers_json)
    st.json({"未保存回答：":session_state.temp_answers,"已保存回答：":session_state.all_answers})

if __name__ == "__main__":
    main()
