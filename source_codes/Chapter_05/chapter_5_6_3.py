st_scores["English"]

st_scores_rec = st_scores.view(np.recarray)

st_scores_rec.English

%timeit st_scores["English"]

%timeit st_scores_rec["English"]

%timeit st_scores_rec.English

