import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="상원고 순열 방탈출", page_icon="🔐", layout="centered")

# 학생들의 현재 스테이지를 기억하는 저장소 만들기
if 'stage' not in st.session_state:
    st.session_state.stage = 1
if 'stage1_unlocked' not in st.session_state:
    st.session_state.stage1_unlocked = False

st.title("🔐 상원고 순열 방탈출!")

# ==========================================
# STAGE 1: 기본 방탈출
# ==========================================
if st.session_state.stage == 1:
    st.info("🔓 STAGE 1: 아래 3개의 미션을 모두 해결하고 첫 번째 금고를 여세요!")
    st.divider()
    
    st.subheader("📌 미션 1")
    st.write("상원고 축제 홍보대사로 남학생 3명과 여학생 3명이 일렬로 서려고 합니다. 남학생과 여학생이 **서로 번갈아 교대로** 서는 경우의 수는 몇 가지일까요?")
    q1 = st.text_input("미션 1 정답:", key="q1")

    st.subheader("📌 미션 2")
    st.write("1학년 3명과 2학년 4명이 일렬로 서서 급식을 기다립니다. **1학년 3명은 어느 누구도 서로 이웃하지 않게** 서는 경우의 수는 몇 가지일까요?")
    q2 = st.text_input("미션 2 정답:", key="q2")

    st.subheader("📌 미션 3")
    st.write("영어 단어 **'SPECIAL'**의 7개 문자를 일렬로 나열할 때, **'S'와 'P'는 서로 이웃**하고, **양 끝에는 모두 모음(E, I, A)**이 오도록 나열하는 경우의 수는 몇 가지일까요?")
    q3 = st.text_input("미션 3 정답:", key="q3")

    st.divider()

    if st.button("🗝️ 1단계 금고 열기!", use_container_width=True):
        if q1 == "72" and q2 == "1440" and q3 == "288":
            st.session_state.stage1_unlocked = True
            st.rerun()
        else:
            st.error("❌ 삐빅! 암호가 틀렸습니다. 다시 고민해보세요!")

    if st.session_state.stage1_unlocked:
        st.success("🎉 찰칵! 첫 번째 금고가 열렸습니다!")
        st.balloons()
        st.info("아쉽죠? 우리 금고 하나 더 열어볼까요?")
        if st.button("🗝️ 2단계 금고 열러 가기", use_container_width=True):
            st.session_state.stage = 2
            st.session_state.stage1_unlocked = False
            st.rerun()


# ==========================================
# STAGE 2: 보너스 방탈출
# ==========================================
elif st.session_state.stage == 2:
    st.info("💎 STAGE 2: 보너스 미션! 1탄을 깬 실력자들을 위한 전설의 금고입니다.")
    st.divider()
    
    st.subheader("📌 보너스 미션 1")
    st.write("밴드부 보컬 2명과 악기 연주자 4명(총 6명)이 일렬로 섭니다. **드럼 연주자는 맨 왼쪽 끝에 서고, 보컬 2명은 서로 이웃하게** 서는 경우의 수는 몇 가지일까요?")
    q4 = st.text_input("보너스 미션 1 정답:", key="q4")

    st.subheader("📌 보너스 미션 2")
    st.write("매점 줄에 1학년 2명, 2학년 3명, 3학년 2명이 일렬로 서 있습니다. **같은 학년끼리 서로 이웃하게** 서는 경우의 수는 몇 가지일까요?")
    q5 = st.text_input("보너스 미션 2 정답:", key="q5")

    st.subheader("📌 보너스 미션 3")
    st.write("사물함 4자리 비밀번호를 1부터 9까지의 서로 다른 숫자로 만들 때, **양 끝의 숫자가 모두 짝수(2, 4, 6, 8)**가 되는 경우의 수는 몇 가지일까요?")
    q6 = st.text_input("보너스 미션 3 정답:", key="q6")

    st.divider()

    if st.button("🗝️ 전설의 금고 열기!", use_container_width=True):
        if q4 == "48" and q5 == "144" and q6 == "504":
            st.success("🎉 철칵! 전설의 금고까지 완벽하게 열렸습니다!")
            st.balloons()
            st.session_state.stage = 3
            st.rerun()
        else:
            st.error("❌ 삐빅! 암호가 틀렸습니다. 보너스 금고는 호락호락하지 않습니다!")


# ==========================================
# STAGE 3: 최종 성공 화면
# ==========================================
elif st.session_state.stage == 3:
    st.balloons()
    st.markdown("<h2 style='text-align: center; color: #bc84ee;'>🏆 MISSION CLEAR! 🏆</h2>", unsafe_allow_html=True)
    st.success("모든 방탈출에 성공했습니다! 선생님께 이 화면을 보여주고 최고급 간식을 받으세요!")
    
    if st.button("🔄 처음부터 다시 하기", use_container_width=True):
        st.session_state.stage = 1
        st.rerun()
