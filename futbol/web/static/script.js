
function getTeams(leagueName, teamName){
    let teamsContainer = document.getElementById(teamName);
    let xhr = new XMLHttpRequest();

    xhr.open('GET', 'https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l='+leagueName);

    xhr.send();

    xhr.addEventListener('load', function(){
        let data = JSON.parse(xhr.responseText);
        let team_id;

        for(let i=0; i < data.teams.length; i++){
            if (data.teams[i].strTeam == teamName) {
                team_id = i;
            }
        }
        
        let html = `        
            <img src="${data.teams[team_id].strTeamBadge}" />
        `;
        
        teamsContainer.insertAdjacentHTML("beforebegin", html);
    });
}

