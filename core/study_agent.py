import agentscope
from agentscope.agents.user_agent import UserAgent
from agentscope.message import Msg
from agentscope.msghub import msghub
from functools import partial
from agentscope.agents import DialogAgent
from core.prompt import Prompts as pr

HostMsg = partial(Msg, name="Moderator", role="assistant", echo=True)

agentscope.init(
    model_configs="configs/model_config.json",
)

# initialize agents
# todo：initialize the agent with config file
planner_agent = DialogAgent(
    name="Plan maker",
    sys_prompt=pr.plan_prompt,
    model_config_name="tongyi_qwen_config",
    use_memory=True,
)
# todo：challenger_agent

teacher_agent = DialogAgent(
    name="Teacher",
    sys_prompt=pr.teacher_prompt,
    model_config_name="tongyi_qwen_config",
)

QA_agent = DialogAgent(
    name="QA Teacher",
    sys_prompt=pr.qa_prompt,
    model_config_name="tongyi_qwen_config",
)

Exam_agent = DialogAgent(
    name="Exam Teacher",
    sys_prompt=pr.exam_prompt,
    model_config_name="tongyi_qwen_config",
)

ans_gen_agent = DialogAgent(
    name="Answer Teacher",
    sys_prompt=pr.answer_prompt,
    model_config_name="tongyi_qwen_config",
)

marker_agent = DialogAgent(
    name="Mark Teacher",
    sys_prompt=pr.mark_prompt,
    model_config_name="tongyi_qwen_config",
)
user_agent = UserAgent()


def main() -> None:
    intro = HostMsg(content="您好，我是夫子，您的智能学习助手。请告诉我您希望学习哪方面的知识。")
    roles = [planner_agent, teacher_agent, QA_agent, Exam_agent, ans_gen_agent, marker_agent, user_agent]
    with msghub(participants=roles, announcement=intro) as tea2stu:
        # step1:user put up the purpose and make a learning plan
        purpose = user_agent()
        teacher_agent.observe(purpose)
        plan = planner_agent(purpose)

        # step2:teach!
        # todo:check schedule
        classes = teacher_agent(plan)

        # todo:check if need qa

        # step3: generate exam and answer
        exam_hint = HostMsg(content=f"课程学习完成，接下来我们将检测一下您的掌握程度")
        tea2stu.broadcast(exam_hint)

        exam = Exam_agent(classes)
        stu_answer = user_agent()
        score = marker_agent(stu_answer)
        answer = ans_gen_agent(exam)

        # todo:according the score,decide whether to continue

if __name__ == "__main__":
    main()
