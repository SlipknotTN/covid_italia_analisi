# Covid Italia analisi dati

Fonte: [dati protezione civile](https://github.com/pcm-dpc/COVID-19)

## Istruzioni

- Clonare il [repository con i dati della Protezione Civile](https://github.com/pcm-dpc/COVID-19) 
  in una directory locale
- Scaricare i dati aggiornati (i dati sono aggiornati giornalmente) con lo script
  update_dati_prociv.sh <prociv_repo_local_dir>
- Lanciare il server jupyter notebook ed accedere agli stessi, all'interno sarà necessario settare
  il path <prociv_repo_local_dir> per il recupero dei dati

## Mancanze note nei dati

- Nuovi ricoverati (si ha il dato dei ricoverati attuali ed dei dimessi guariti)
- I dati provinciali contengono solo i dati cumulati dei positivi
- I dati sulle zone di colore regionali sono incompleti / da incrociare con le zone nazionali
