import streamlit as st


        

class dnfCalc:
    def __init__(self, buf_name, dealer1, dealer2, dealer3, **kwargs):
        self.buf_name = buf_name
        self.dealers = [dealer1, dealer2, dealer3]
        
        self.party_str = 0.0
        self.new_party = []
        
        
        self.noaria = 1.15
        self.nopupet = 1.25
        self.noad = 1.1    
        
        self.three_party = False
        
        self.number_tag = ["1", "2", "3"]
        self.bool_piper = False
        self.piper_deal = 0.0

        
        

    def calculate(self, buf_str):
        
        if self.buf_name == "헤카테":
            self.buf_str_std4 = buf_str
            self.buf_str_heart = round(buf_str * 1.117867, 1)
            self.buf_str_noheart = ((self.buf_str_std4 * 3) - self.buf_str_heart) / 2

            for idx, i in enumerate(self.dealers, start=1):
                dealer_tag = f"딜러{idx}"

                # 1) 기본 버프 적용
                if heart == dealer_tag:
                    val = round(i * (self.buf_str_heart / 500), 2)
                else:
                    val = round(i * (self.buf_str_noheart / 500), 2)

                # 2) 파이퍼 보정(노퍼펫)
                if piper == dealer_tag:
                    val = round(val / self.nopupet, 2)
                    self.bool_piper = True
                    self.piper_deal = val   # ✅ 최종값 저장

                self.party_str += val
                self.new_party.append(val)
                
        # if self.buf_name == "헤카테":
        #     self.buf_str_std4 = buf_str
        #     self.buf_str_heart = round(buf_str*1.117867, 1)
        #     self.buf_str_noheart = ((self.buf_str_std4*3) - self.buf_str_heart) / 2             # 노편애 버프력
        #                                         # 편애버프력
            

        #     for idx, i in enumerate(self.dealers, start=1):
        #         if heart == f"딜러{idx}":
        #             self.big_dealer = round((i * (self.buf_str_heart) / 500), 2)
                    
                    
        #             if piper == f"딜러{idx}":
        #                 self.piper_deal = self.big_dealer
        #                 self.big_dealer = self.big_dealer / self.nopupet
        #                 self.bool_piper = True 
                    
        #             self.party_str += self.big_dealer
        #             self.new_party.append(self.big_dealer)

                
                # else:
                #     self.ntr_dealer = round((i * (self.buf_str_noheart) / 500), 2)
                    
                #     if piper == f"딜러{idx}":
                #         self.piper_deal = self.dealers[idx-1]
                #         self.ntr_dealer = self.ntr_dealer / self.nopupet
                #         self.bool_piper = True
                    
                    
                #     self.party_str += self.ntr_dealer
                #     self.new_party.append(self.ntr_dealer)
                    
            
        elif self.buf_name == "뮤즈":
            for idx, i in enumerate(self.dealers, start=1):
                dealer_tag = f"딜러{idx}"
                val = round(i * (buf_str / 500), 2)

                if piper == dealer_tag:
                    # ✅ 오프바이원 수정: dealers[idx-1]
                    original = self.dealers[idx-1]
                    val = round(val / self.noad, 2)
                    self.bool_piper = True
                    self.piper_deal = val

                self.party_str += val
                self.new_party.append(val)    
                
                
                
        # elif self.buf_name == "뮤즈":
        #     for idx, i in enumerate(self.dealers, start =1):
        #         buf_muse = round(i * (buf_str / 500), 2)
                
        #         if piper == f"딜러{idx}":
        #             self.piper_deal = self.dealers[idx-1]
        #             self.party_str += (buf_muse / self.noad)
        #             self.new_party.append(buf_muse / self.noad)
        #             self.bool_piper = True 
        #         else:
        #             self.party_str += buf_muse     
        #             self.new_party.append(buf_muse)
        elif self.buf_name == "크루세이더(여)":
            for idx, i in enumerate(self.dealers, start=1):
                dealer_tag = f"딜러{idx}"
                val = round(i * (buf_str / 500), 2)

                if piper == dealer_tag:
                    # ✅ 여크루는 노아리아
                    original = self.dealers[idx-1]
                    val = round(val / self.noaria, 2)
                    self.bool_piper = True
                    self.piper_deal = val

                self.party_str += val
                self.new_party.append(val)
        
        
                    
        # elif self.buf_name == "크루세이더(여)":
        #     for idx, i in enumerate(self.dealers, start=1):
        #         buf_evan = round(i * (buf_str / 500), 2)
                
        #         if piper == f"딜러{idx}":
        #             self.piper_deal = self.dealers[idx-1]
        #             self.party_str += (buf_evan / self.noaria)
        #             self.new_party.append(buf_evan / self.noaria)
        #             self.bool_piper = True   
        #         else:
        #             self.party_str += buf_evan     
        #             self.new_party.append(buf_evan)
                    
        
        else:  # 크루세이더(남) or 메딕 등
            for idx, i in enumerate(self.dealers, start=1):
                dealer_tag = f"딜러{idx}"
                val = round(i * (buf_str / 500), 2)

                if piper == dealer_tag:
                    # 현재 규칙상 추가 보정 없음
                    self.bool_piper = True
                    self.piper_deal = val

                self.party_str += val
                self.new_party.append(val)

        return round(sum(self.new_party), 1)
                
    
            

    def prt(self):
        print(f"각 딜러 계산결과 : {self.new_party}")
        print("총 파티 화력 : ", sum(self.new_party))





st.title("던파 파티 화력 측정기")
st.markdown("""
파티 내 딜러들의 딜량과 버퍼의 버프력을 바탕으로  
**실제 적용된 총 파티 화력**을 계산해줍니다.
※ 이내황혼전 500버퍼 기준으로 작성되었습니다.            
""")

muri = False
muri1 = False
muri2 = False
muri3 = False


buf_name = st.selectbox("버퍼 타입을 선택하세요", ["헤카테", "뮤즈", "크루세이더(여)","크루세이더(남), 메딕"])


buf_str = st.number_input("버프력 (예: 500)", value=500.0)
st.caption("※ 헤카테의 버프력은 던담 4인 기준입니다.")
dealer1 = st.number_input("딜러 1 딜량 (단위 : 억)", value=100.0)
if st.checkbox("딜러1 무리시너지 여부"):
    muri1 = True
dealer2 = st.number_input("딜러 2 딜량 (단위 : 억)", value=100.0)

if st.checkbox("딜러2 무리시너지 여부"):
    muri2 = True
dealer3 = st.number_input("딜러 3 딜량 (단위 : 억)", value=100.0)

if st.checkbox("딜러3 무리시너지 여부"):
    muri3 = True
    


muri = muri1 or muri2 or muri3
boost = 1.08 if muri else 1.0


piper = st.radio(
    "1인딜러 (파이퍼)",
    ["x", "딜러1", "딜러2", "딜러3"])   # 노편애 노퍼펫 노아리아 노아드


if buf_name == "헤카테":
    heart = st.radio(
        "편애 딜러 선택",
        ["x", "딜러1", "딜러2", "딜러3"]
    )




dft = 300       # 100/500 에서의 100 딜컷*3

if muri == True:
    boost = 1.08
else:
    boost = 1.0
    



if st.button("계산하기"):
    model = dnfCalc(buf_name, dealer1, dealer2, dealer3)
    result = model.calculate(buf_str)
    
    st.subheader("📊 딜 기댓값")
    
    
    piper_idx = None
    if piper != "x":
        try:
            piper_idx = int(piper[-1])
        except:
            piper_idx = None
    
    muri_flags = [muri1, muri2, muri3]
    three_party_idxs = [i for i in [1, 2, 3] if i != piper_idx] if piper_idx else [1, 2, 3]
    three_has_muri = any(muri_flags[i-1] for i in three_party_idxs)
    piper_is_muri = (piper_idx is not None) and muri_flags[piper_idx-1]
    
    
    
    boosted_each = []
    piper_boosted = 0.0
        
    for i, val in enumerate(model.new_party, 1):
        if piper_idx is not None and i == piper_idx:
            # 싱글(파이퍼): 무리면 ×1.181, 아니면 그대로
            boost_val = val * (1.181 if piper_is_muri else 1.0)
        else:
            # 3인 파티: 파티 내에 무리 1명이라도 있으면 전원 ×1.08
            boost_val = val * (1.08 if three_has_muri else 1.0)
        boosted_each.append(boost_val)
        tag = "(파이퍼)" if (piper_idx is not None and i == piper_idx) else ""
        st.write(f"딜러{i}: {boost_val:.2f} {tag}")

    boosted_total = sum(boosted_each)

    # 6) 출력(3인/1인 분리)
    if piper_idx is not None:
        piper_boosted = boosted_each[piper_idx-1]
        three_party_boosted = boosted_total - piper_boosted
        st.success(f"3인 파티 화력: {three_party_boosted:.2f}")
        st.success(f"1인 싱글 화력 : {piper_boosted:.2f}")
        st.success(f"4인 파티 화력 : {boosted_total:.2f}")
    else:
        st.success(f"총 파티 화력: {boosted_total:.2f}")

    dft = 300
    st.caption("100/500 파티 기준")
    st.success(f"{(boosted_total / dft) * 100:.2f}%")    
        
        
    # for i, val in enumerate(model.new_party, 1):
        
    #     tag = ""
    #     boost_val = val
    #     dealer_tag = f"딜러{i}"
        
    #     if piper == dealer_tag:     # 만약 piper == 딜러1, 딜러2... 딜러3 이라면
    #         tag = "(파이퍼)"
            
    #         if (i == 1 and muri1) or (i == 2 and muri2) or (i==3 and muri3):            # 파이퍼파티가 무리인경우
    #             boost_val = val*1.181
    #         piper_boosted = boost_val
    #     else:                                                                           # 파이퍼파티가 무리가 아닌경우
    #         if (i == 1 and muri1) or (i == 2 and muri2) or (i == 3 and muri3):
    #             boost_val = val * 1.08
        
    #     boost_each.append(boost_val)
    #     st.write(f"딜러{i}: {boost_val:.2f} {tag}")     
    
    # boost_total = sum(boost_each)
    
    
    
    # if model.bool_piper:
    #     st.success(f"3인 파티 화력: {(boost_total - piper_boosted):.2f}")
    #     st.success(f"1인 싱글 화력 : {piper_boosted:.2f}")
    #     st.success(f"총 파티 화력: {boost_total:.2f}")
    # else:
    #     st.success(f"총 파티 화력: {boost_total:.2f}")
    
    
    
    
    # st.caption("100/500 파티 기준")
    # st.success(f"{(boost_total / dft) * 100:.2f}%")
    
    # if model.bool_piper == True:
    #     for i, val in enumerate(model.new_party, 1):
    #         if piper == f"딜러{i}":
    #             st.write(f"딜러{i}: {val*(boost):.2f} (싱글)")
    #         else:
    #             st.write(f"딜러{i}: {val*(boost):.2f}")
        
    
    #     st.success(f"3인 파티 화력: {(result - model.piper_deal):.2f}")
    #     st.success(f"1인 싱글 화력 : {model.piper_deal:.2f}")
    #     st.success(f"4인 파티 화력 : {result:.2f}")
        
    # else:
    #     for i, val in enumerate(model.new_party, 1):
    #         st.write(f"딜러{i}: {val*(boost):.2f}")

        
    #     st.caption("100/500 파티 기준")
    #     st.success(f"{(result / dft) * 100:.2f}%")






# model1 = dnfCalc("m", 30,30,30)
# model1.calculate(380)
# model1.prt()