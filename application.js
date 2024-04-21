function addMember() {
    var container = document.getElementById("teamMembers");
    var memberDiv = document.createElement("div");
    memberDiv.className = "team-member";
    memberDiv.innerHTML = '<input type="text" class="form-control" name="teammateName[]" placeholder="Teammate Name">';
    container.appendChild(memberDiv);
}

