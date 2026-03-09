import streamlit as st

st.set_page_config(
    page_title="CAECO - Chapa LASTRO",
    layout="wide"
)

#tela inicial
def funcao_nova():
    pass

def opcoes_menu():
    col1, col2 = st.columns([1, 8])
    st.header("Portal CAECO")
    st.subheader("Centro Acadêmico de Economia do Campus Avançado UFJF-GV", divider= True)

    with st.sidebar:
        col1, col2 = st.columns([3,6])
        with col1:
            st.image("logo_caeco.png", width=100)
        with col2:
            st.markdown("## :blue[CAECO] :blue[UFJF-GV]")

        if st.button('Integrantes', key = 'integrantes_caeco'):
            st.session_state.tela = 'integrantes'
            st.rerun()

        st.markdown("---")
        st.caption("Versão 1.0 • 2026")
        st.caption("© CAECO - UFJF GV. Chapa Lastro - Todos os direitos reservados")
    
    st.write("Fique por dentro de todas as ações realizadas!")
    lista_caeco1 = ['Portal de Transparência','Objetivos, Missões e Valores',
                       'Plano de Gestão','Semana de Economia XI',
                           'Loja CAECO','Manual de Sobrevivência do Calouro','Patrocinadores']
    
    opcoes = st.selectbox("Acessar: ", lista_caeco1)
    if st.button("Acessar", key = 'enter_caeco_list', type='primary'):
        nome_tela = opcoes.lower().replace(' ', '_').replace(',', '')
        st.session_state.tela = nome_tela
        st.rerun()

def chapa_lastro():
    st.header("Conheça os integrantes da CHAPA LASTRO de 2026")
    voltar()

def portal_transparencia():
    st.title("Portal de Transparência")
    st.write("Aqui entram os dados financeiros do CAECO.")
    voltar()

def voltar(chave):
    if st.button('Voltar', key = chave, type = 'secondary'):
        st.session_state.tela = 'menu'
        st.rerun()
def main():
    if 'tela' not in st.session_state:
        st.session_state.tela = 'menu'

    match st.session_state.tela:
        case 'menu':
            opcoes_menu()
        case 'integrantes':
            chapa_lastro()
        case 'portal_de_transparência':
            portal_transparencia()
        case _:
            st.warning(f"A tela '{st.session_state.tela}' ainda está em construção!")
            voltar()

#loop 
if __name__ == "__main__":
    main()

