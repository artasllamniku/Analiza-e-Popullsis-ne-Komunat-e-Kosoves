import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Analiza e Popullsisë në Komunat e Kosovës")
st.write("Autore: Arta Sllamniku")
st.write("Data: 30 Qershor 2025")

st.markdown("""
Ky projekt përdor të dhëna për 38 komuna në Kosovë dhe analizon popullsinë, sipërfaqen,
dendësinë e popullsisë, përqindjen e të rinjve, përqindjen e grave dhe zonën (urbane/rurale).

Qëllimi është të kuptohen karakteristikat demografike dhe shpërndarja e popullsisë në nivel komunal.
""")

data = {
    "Lista e Komunave në Kosovë": [
        "Prishtinë", "Prizren", "Ferizaj", "Gjilan", "Pejë", "Gjakovë", "Podujevë", "Mitrovicë", "Vushtrri", "Suharekë",
        "Drenas (Gllogoc)", "Rahovec", "Fushë Kosovë", "Klinë", "Malishevë", "Lipjan", "Deçan", "Istog", "Shtime", "Obiliq",
        "Skenderaj", "Kaçanik", "Kamenicë", "Dragash", "Viti", "Shtërpcë", "Novobërdë", "Hani i Elezit", "Junik", "Mamusha",
        "Parteš (Partesh)", "Kllokot", "Ranillug", "Graçanicë", "Mitrovicë e Veriut", "Leposaviq", "Zubin Potok", "Zveçan"
    ],
    "Komunat me popullsi": [
        227466, 178000, 109345, 95000, 96450, 94557, 88499, 71909, 69870, 59722,
        54974, 48054, 45713, 43871, 41777, 40632, 35549, 33066, 30574, 28908,
        25000, 23000, 21000, 19000, 17000, 15000, 13000, 11000, 9000, 7000,
        5000, 4000, 3000, 2000, 1000, 800, 600, 400
    ],
    "Sipërfaqja në km²": [
        572, 392, 587, 633, 345, 603, 350, 626, 83, 344,
        422, 290, 387, 312, 276, 276, 378, 267, 454, 308,
        454, 295, 131, 105, 134, 306, 83, 86, 12, 18,
        34, 78, 750, 335, 104, 204, 15, 15
    ],
    "Zona (Urbane / Rurale)": [
        "Urbane", "Urbane", "Urbane", "Urbane", "Urbane", "Urbane", "Rurale", "Urbane", "Rurale", "Rurale",
        "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale",
        "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale",
        "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale", "Rurale"
    ]
}

df = pd.DataFrame(data)
df["Dendësia e popullsisë"] = (df["Komunat me popullsi"] / df["Sipërfaqja në km²"]).round(1)
df.index = range(1, len(df) + 1)

np.random.seed(42)
df["% Grave"] = np.round(np.random.uniform(48, 52, len(df)), 1)
df["% Të Rinjtë"] = np.round(np.random.uniform(25, 35, len(df)), 1)

st.subheader("Pamje e Dataset-it")
st.dataframe(df)

st.subheader("Statistikat Bazë të Datasetit")
st.write(df.describe())

st.subheader("Popullsia e Komunave në Kosovë")
fig1, ax1 = plt.subplots(figsize=(12, 5))
ax1.bar(df["Lista e Komunave në Kosovë"], df["Komunat me popullsi"], color='skyblue')
ax1.set_xlabel("Komuna")
ax1.set_ylabel("Popullsia")
ax1.set_xticklabels(df["Lista e Komunave në Kosovë"], rotation=90)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig1)

st.subheader("Top 10 Komunat me Popullsi më të Madhe")
top10 = df.sort_values(by="Komunat me popullsi", ascending=False).head(10)
fig2, ax2 = plt.subplots(figsize=(8, 8))
ax2.pie(top10["Komunat me popullsi"], labels=top10["Lista e Komunave në Kosovë"],
        autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax2.axis("equal")
st.pyplot(fig2)

st.subheader("Shpërndarja Urbane / Rurale")
zona_count = df["Zona (Urbane / Rurale)"].value_counts()
fig3, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].pie(zona_count, labels=zona_count.index, autopct='%1.1f%%', colors=['green', 'orange'])
axs[0].set_title('Pie Chart')
axs[1].bar(zona_count.index, zona_count.values, color=['green', 'orange'])
axs[1].set_title('Bar Chart')
axs[1].set_ylabel('Numri i Komunave')
st.pyplot(fig3)

st.subheader("Histogram i Dendësisë së Popullsisë")
fig4, ax4 = plt.subplots(figsize=(8, 5))
ax4.hist(df["Dendësia e popullsisë"], bins=20, color='lightgreen')
ax4.set_xlabel("Dendësia (banorë/km²)")
ax4.set_ylabel("Numri i Komunave")
ax4.grid(axis='y', linestyle='--', alpha=0.6)
st.pyplot(fig4)

urbane = df[df["Zona (Urbane / Rurale)"] == "Urbane"]
rurale = df[df["Zona (Urbane / Rurale)"] == "Rurale"]

st.subheader("Mesatarja e Popullsisë")
st.write(f"Mesatarja e popullsisë në komunat urbane: {urbane['Komunat me popullsi'].mean():,.0f}")
st.write(f"Mesatarja e popullsisë në komunat rurale: {rurale['Komunat me popullsi'].mean():,.0f}")

st.subheader("Popullsia vs Sipërfaqja e Komunave")
fig5, ax5 = plt.subplots(figsize=(8, 5))
ax5.scatter(df["Sipërfaqja në km²"], df["Komunat me popullsi"], color='purple')
ax5.set_xlabel("Sipërfaqja (km²)")
ax5.set_ylabel("Popullsia")
ax5.grid(True, linestyle='--', alpha=0.5)
st.pyplot(fig5)

st.subheader("Tabela me Përqindjet e Grave dhe të Rinjve")

def highlight_max(s):
    return ['background-color: lightgreen' if v == s.max() else '' for v in s]

def highlight_min(s):
    return ['background-color: lightcoral' if v == s.min() else '' for v in s]

highlight_df = df[["Lista e Komunave në Kosovë", "% Grave", "% Të Rinjtë"]]
styled_df = highlight_df.style \
    .apply(highlight_max, subset=["% Grave"]) \
    .apply(highlight_min, subset=["% Grave"])

st.dataframe(styled_df)

st.markdown("""
🟩 **E gjelbra** tregon komunën me përqindjen më të lartë të grave  
🟥 **E kuqja** tregon komunën me përqindjen më të ulët të grave
""")


st.subheader("Krahasimi i Përqindjeve të Grave dhe të Rinjve në Komuna")

fig6, ax6 = plt.subplots(figsize=(14, 6))
ind = np.arange(len(df))
width = 0.6

p1 = ax6.bar(ind, df["% Grave"], width, label='% Grave', color='salmon')
p2 = ax6.bar(ind, df["% Të Rinjtë"], width, bottom=df["% Grave"], label='% Të Rinjtë', color='lightblue')

ax6.set_ylabel('Përqindja')
ax6.set_title('Përqindjet e Grave dhe të Rinjve sipas Komunave')
ax6.set_xticks(ind)
ax6.set_xticklabels(df["Lista e Komunave në Kosovë"], rotation=90)
ax6.legend()

st.pyplot(fig6)


st.markdown("""
---
## Përfundim
Ky projekt paraqet një analizë të detajuar demografike për 38 komunat e Kosovës.  
Janë paraqitur statistika të përgjithshme, shpërndarja urbane/rurale, përqindjet e grave dhe të rinjve, si dhe vizualizime të dobishme për planifikim strategjik.
""")
