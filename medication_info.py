pip install streamlit openai
import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Streamlit 앱 제목
st.title("약학 정보 검색기")

# 사용자 입력 받기
medication = st.text_input("약물 이름을 입력하세요:")

# 입력된 약물 이름이 있을 때만 API 호출
if medication:
    # OpenAI API를 통해 ChatGPT에게 질문하기
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"다음 약물에 대한 정보를 알려줘: {medication}",
        max_tokens=150,
        temperature=0.7
    )
    
    # 응답에서 텍스트 추출
    information = response.choices[0].text.strip()
    
    # 결과 출력
    st.subheader("약물 정보")
    st.write(information)
else:
    st.write("약물 이름을 입력하세요.")
