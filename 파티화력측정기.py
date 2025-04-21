import streamlit as st


class dnfCalc:
    def __init__(self, buf_name, dealer1, dealer2, dealer3, **kwargs):
        self.buf_name = buf_name
        self.dealers = [dealer1, dealer2, dealer3]
        
        self.party_str = 0
        self.new_party = []
    
    def calculate(self, buf_str):
        
        if self.buf_name == "헤카테":
            self.buf_str_std4 = buf_str
            self.buf_str_heart = round(buf_str*1.117867, 1)
            self.buf_str_noheart = (self.buf_str_std4*3 - self.buf_str_heart) / 2
            
            self.max_dealer = max(self.dealers)
            self.max_idx = self.dealers.index(self.max_dealer)

            for idx, i in enumerate(self.dealers):
                if idx == self.max_idx:
                    self.big_dealer = round((self.dealers[idx] * (self.buf_str_heart / 400)), 2)
                    self.party_str += self.big_dealer
                    self.new_party.append(self.big_dealer)
                    
                else:
                    self.ntr_dealer = round((self.dealers[idx] * (self.buf_str_noheart/ 400)), 2)
                    self.party_str += self.ntr_dealer 
                    self.new_party.append(self.ntr_dealer)
        
        else:
            for j in self.dealers:
                self.party_str += j
                self.new_party.append(round(j*(buf_str/400), 2))




            
                    
    
        return round(sum(self.new_party), 1)
            

    def prt(self):
        print(f"각 딜러 계산결과 : {self.new_party}")
        print("총 파티 화력 : ", sum(self.new_party))



# def main():
#     print("🔧 던파 파티 딜 계산기")
#     buf_name = input("버퍼 종류를 입력하세요 (예: h, seraphim, enchant): ").strip()
#     buf_str = float(input("버프력을 입력하세요 (ex: 400): "))

#     print("\n각 딜러의 개인 딜량을 입력하세요")
#     dealer1 = float(input("딜러1 딜량: "))
#     dealer2 = float(input("딜러2 딜량: "))
#     dealer3 = float(input("딜러3 딜량: "))

#     model = dnfCalc(buf_name, dealer1, dealer2, dealer3)
#     model.calculate(buf_str)
#     model.prt()
        

# if __name__ == "__main__":
#     main()


st.title("던파 파티 화력 측정기")

buf_name = st.selectbox("버퍼 타입을 선택하세요", ["헤카테", "뮤즈", "크루세이더(여)","크루세이더(남)"])
buf_str = st.number_input("버프력 (예: 400)", value=400.0)

dealer1 = st.number_input("딜러 1 딜량", value=30.0)
dealer2 = st.number_input("딜러 2 딜량", value=30.0)
dealer3 = st.number_input("딜러 3 딜량", value=30.0)

if st.button("계산하기"):
    model = dnfCalc(buf_name, dealer1, dealer2, dealer3)
    result = model.calculate(buf_str)
    
    st.subheader("📊 딜 결과")
    for i, val in enumerate(model.new_party, 1):
        st.write(f"딜러{i}: {val}")
    st.success(f"총 파티 화력: {result}")







# model1 = dnfCalc("m", 30,30,30)
# model1.calculate(380)
# model1.prt()