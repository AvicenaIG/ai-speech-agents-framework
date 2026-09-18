from dataclasses import dataclass, field

from ai_speech_agents_framework.arguments_classes.language_model_base_arguments import LanguageModelBaseArguments

MLX_DEFAULT_LM_MODEL = "mlx-community/Qwen3.5-4B-4bit"


@dataclass
class LanguageModelHandlerArguments(LanguageModelBaseArguments):
    pass  # TODO: implement


@dataclass
class MLXLanguageModelHandlerArguments(LanguageModelHandlerArguments):
    pass  # TODO: implement
