
let teamsContainer = document.getElementsByClassName('team');
function getTeams(countryName, teamName){
    let xhr = new XMLHttpRequest();

    xhr.open('GET', 'https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?s=Soccer&c='+countryName);

    xhr.send();

    xhr.addEventListener('load', function(){
        let data = JSON.parse(xhr.responseText);
        let team_id = 0;

        for(let i=0; i < data.teams.length; i++){
            if (data.teams[i].strTeam == teamName) {
                team_id = i;
            }
        }
        
        let html = `        
        <article class="team">
            <img class="team_img" src="${data.teams[team_id].strTeamBadge}" />
            <div class="team_data">
                <h3 class="team_name">${data.teams[team_id].strTeam}</h3>
                <h4 class="team_region">${data.teams[team_id].strCountry}</h4>
            </div>
        </article>
        `;
        
        document.getElementById('team').insertAdjacentHTML("afterend", html);
    });
}


let teamsContainer = document.getElementsByClassName('team');
function getTeams(countryName, teamName){
    let xhr = new XMLHttpRequest();

    xhr.open('GET', 'https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?s=Soccer&c='+countryName);

    xhr.send();

    xhr.addEventListener('load', function(){
        let data = JSON.parse(xhr.responseText);
        let team_id = 0;

        for(let i=0; i < data.teams.length; i++){
            if (data.teams[i].strTeam == teamName) {
                team_id = i;
            }
        }
        
        let html = `        
        <article class="team">
            <img class="team_img" src="${data.teams[team_id].strTeamBadge}" />
            <div class="team_data">
                <h3 class="team_name">${data.teams[team_id].strTeam}</h3>
                <h4 class="team_region">${data.teams[team_id].strCountry}</h4>
            </div>
        </article>
        `;
        
        document.getElementById('team').insertAdjacentHTML("afterend", html);
    });
}

