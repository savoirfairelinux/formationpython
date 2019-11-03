def calculer_taxes(montant, taux_tps=0.05, taux_tvq=0.09975):
    tps = montant * taux_tps
    tvq = montant * taux_tvq
    return tps + tvq
