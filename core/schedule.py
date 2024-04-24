class Schedule:
    """
    To manage the lifecycle of study schedule
    """
    def __init__(self):
        self. =

    def plan(self, agent, purpose):
        """
        According to the user's input,make the plan.
        :return:list
        """
        try:
            # todo:make agent's output into list,by prompt
            plan = agent(purpose)
            # todo:format the result into tree(list)
            actually_schedule = plan.content
        except e:

        return actually_schedule

    def del_node(self, content):
        """
        When user dont want to learn the content,del it in original schedule.
        :return:
        """

    def check_schedule(self, actually_schedule, current_class):
        """
        Check the schedule.
        :return:
        """
        next_class = None
        for i in len(actually_schedule)-1:
            if actually_schedule[i] is current_class:
                next_class = actually_schedule[i+1]
        return next_class

    def update(self):
        """
        Update the schedule,when it has been changed.
        :return:
        """


[["1. xxx" ["1.1 xxx"],["1.2 xxx"],]]