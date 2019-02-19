enum Units {
	CM,	//centimetre
	MM, //milimetre
	IN, //inch
	PT, //point (1/72 inch)
	PX, //pixel
	EM, //em-size
	EN, //en-size
	PC	//percentage
}

class Unit {
	Units unit
	float value
	Unit(Units unit, float value) {

	}
	Unit(String unit, float value) {

	}
	Unit(String str) {

	}
}

class Color {

}

enum ElementAlignment {
	LEFT,
	RIGHT,
	CENTERED,
	JUSTIFIED
}

/**
 *
 */
class Document {
	LinkedList<Paragraph> paragraphs
	Document() {
		paragraphs = LinkedList<Paragraph>()
	}
}

/**
 *
 */
class ParagraphStyle {
	double line_spacing
	Unit left, right, top, bottom
}

/**
 *
 */
class Paragraph {

}

class ElementConfiguration {
	Unit left, right, top, bottom //spacing for the element
	enum ElementAlignment alignment
}

/**
 * This is the base class for all that is inscribed in a paragraph.
 */
interface Element {
	//Fill in this element from intermediate representation
	void from_IT(BufferedReader reader)
	//Write intermediate representation to file
	void to_IR(Writer writer)
}

class TextConfiguration {
	String font_name
	Unit font_size
	boolean italic
	boolean bold
	boolean underlined
	boolean striketrough
	Color color
	Color background_color
}

interface TextElement {

}

class Character implements TextElement {
	String character
	Character(String c) {
		character = c
	}
}

class Space implements TextElement {
	boolean breaking
	Unit width
	Space() {
		breaking = false
		width = null
	}
	Space(boolean breaking) {
		this.breaking = breaking
		width = null
	}
	Space(Unit width) {
		breaking = false
		this.width = width
	}
	Space(Unit width, boolean breaking) {
		this.breaking = breaking
		this.width = width
	}

}

class Punctuation implements TextElement {
	String charactter
	Punctuation(String c){
		character = c
	}
}

/**
 *
 */
class Text implements Element {
	TextStyle style
	ArrayList<TextElement> text_elements
	Text(TextStyle style) {
		this.style = style
	}
	Text() {
		text_elements = new ArrayList<TextElement>()
	}
	void add(TextElement elem) {
		text_elements.add(elem)
	}
	ArrayList<TextElement> get() {
		return text_elements
	}
}

class HyperLink implements Element {

}

class Image implements Element {

}

class Table implements Element {

}

class Plot implements Element {

}

class Footnote implements Element {

}

class Equation implements Element {

}
