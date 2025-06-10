import streamlit as st
from module import extract_video_id, get_transcript, summarize_text

# UI Streamlit
st.set_page_config(page_title="Ringkasan YouTube dengan Gemini", layout="centered")
st.title("📺 Ringkasan Video YouTube")
st.markdown("Masukkan URL video YouTube untuk mendapatkan ringkasannya menggunakan Google Gemini.")

url = st.text_input("🔗 Masukkan URL Video YouTube:")

if url:
    video_id = extract_video_id(url)

    if not video_id:
        st.error("❌ URL tidak valid atau tidak dapat menemukan ID video.")
    else:
        try:
            with st.spinner("📄 Mengambil transkrip dan merangkum..."):
                transcript = get_transcript(video_id)
                summary = summarize_text(transcript)

            st.success("✅ Ringkasan berhasil dibuat!")
            st.subheader("📌 Ringkasan:")
            st.write(summary)

        except Exception as e:
            st.error(f"⚠️ Terjadi kesalahan: {e}")
