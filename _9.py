class TeamMember:
    def __init__(self, name, role, skill_level):
        self.name = name
        self.role = role
        self.skill_level = skill_level


class Project:
    def __init__(self, project_name, project_deadline):
        self.project_name = project_name
        self.project_deadline = project_deadline
        self.team_members = []

    def assign_member(self, team_member):
        if team_member in self.team_members:
            print(f"{team_member} has already been assigned to {self.project_name}") 

        else:
            self.team_members.append(team_member)
            print(f"The team member {team_member} has been assigned to the project {self.project_name}")

    def display_project_info(self):
        members = self.team_members if self.team_members else 'No members assigned'
        print(f"Project Name: {self.project_name}\nProject deaadline: {self.project_deadline}\nAssigned members: {members}")

member1 = TeamMember('Jack', 'designer', 7)
member2 = TeamMember('Grace', 'Developer', 6.5)

project1 = Project('System development', '2025-07-12')
project2 = Project('Maintanance', '2025-08-10')
project3 = Project('Debugging', '2026-08-02')

project1.assign_member(member1.name)
project1.assign_member(member2.name)
project2.assign_member(member1.name)

print("-"*60)
project1.display_project_info()
print("-"*60)
project2.display_project_info()
print("-"*60)
project3.display_project_info()