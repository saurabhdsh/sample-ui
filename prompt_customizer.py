class PromptCustomizer:
    def __init__(self, base_prompt="Default prompt"):
        """
        Initializes the PromptCustomizer with a base prompt.
        """
        self.base_prompt = base_prompt

    def customize_prompt(self, additional_info=None, context=None, question=None):
        """
        Customizes the base prompt with additional information, context, and question.
        
        Args:
            additional_info (str): Additional information to include in the prompt.
            context (str): Contextual information to include in the prompt.
            question (str): Specific question to append to the prompt.

        Returns:
            str: The fully customized prompt.
        """
        prompt = self.base_prompt

        if additional_info:
            prompt += f"\nAdditional Info: {additional_info}"
        if context:
            prompt += f"\nContext: {context}"
        if question:
            prompt += f"\nQuestion: {question}"

        return prompt

    def set_base_prompt(self, new_prompt):
        """
        Sets a new base prompt.
        
        Args:
            new_prompt (str): The new base prompt to be set.
            
        Returns:
            str: The updated base prompt.
        """
        self.base_prompt = new_prompt
        return self.base_prompt
