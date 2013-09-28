interface Question {
	question: string;
	help_text: string;
	items: Item[];
};

interface FormConfig {}

interface TextFormConfig extends FormConfig {
	is_multiline: boolean;
};

interface ListFormConfig extends FormConfig {
	options: string[];
	selected: number;
};