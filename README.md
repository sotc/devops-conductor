# devops-conductor
Port and deploy web app service


### Initial Setup
1. make setup
2. source ~/.conductordevops/bin/activate
3. make install

### Containerized app
1. `docker build -t conductor-app:latest .`
2. `docker run -d --env-file ./jwtSecret.env -p 3001:3000 conductor-app`

### Test the app locally
1. `curl -v  http://127.0.0.1:3000/`
2. ` curl -v -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE1NTQ3NTU1NTUsImV4cCI6MjU1NDc1NTUwMCwiaWF0IjoxNTU0NzU1NTAwLCJqdGkiOiI5ZmRmMGE2Ni00YzllLTRlOTktODc4MC05YjdlOTNlMjFlMjciLCJ1c2VyX2lkIjoiMTA1YjM1MTgtNjQ2ZC00NjNlLWFkZGEtZDJiOTM5YzJkMDZkIiwidXNlcl9mdWxsX25hbWUiOiJCZXJ0cmFtIEdpbGZveWxlIiwidXNlcl9lbWFpbCI6Im51bGxAcGllZHBpcGVyLmNvbSJ9.-A8Gx18iTikKpedcxDlgcc7D8GMWFix0709Vfpbo1SI" 127.0.0.1:3001/v1/user/ `
3. `curl -v  http://127.0.0.1:3001/healthz/`
4. Open a web browser: `http://127.0.0.1:3001/docs`