# Regular Expression

## Exercise 1
Use ANTLR to write regular expressions describing a Pascal identifier that must begin with a lowercase letter (’a’ to ’z’), but may continue with many characters which are lowercase letter or digit (’0’ to ’9’).

**For example**:

| Test  | Result    |
|-------|-----------|
| "abc" | abc,<EOF> |

**Answer**:
```antlr
IDENTIFIER: [a-z][a-z0-9]*;
```

## Exercise 2
Use ANTLR to write regular expressions describing Pascal tokens For a number to be taken as "real" (or "floating point") format, it must either have a decimal point, or use scientific notation. For example, 1.0, 1e-12, 1.0e-12, 0.000000001 are all valid reals. At least one digit must exist on either side of a decimal point.

**For example**:

| Test  | Result    |
|-------|-----------|
| "1.0" | 1.0,<EOF> |

**Answer**:
```antlr
FLOAT: DIGIT ('.' DIGIT)? ('e' '-'? DIGIT)?;
fragment DIGIT: [0-9]+;
```

## Exercise 3
Use ANTLR to write regular expressions describing Pascal strings are made up of a sequence of characters between single quotes: 'string'. The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.

**For example**:

| Test  | Result    |
|-------|-----------|
| "'Yanxi Palace - 2018'"| 'Yanxi Palace - 2018',<EOF> |

**Answer**:
```antlr
STRING: '\'' ('\'\'' | ~['])* '\'';
```

## Exercise 4
Khi nhập học tại trường Đại học Bách Khoa, sinh viên được yêu cầu đặt một tên tài khoản gọi là **BKNetID**, gồm ba thành phần theo thứ tự: **tên**, **họ** và **chuỗi tự chọn**. Giữa tên và họ, sinh viên phải đặt một dấu chấm (.). Tên và họ là chuỗi chỉ bao gồm các ký tự chữ thường với độ dài tối thiểu là 1. Chuỗi tự chọn là một chuỗi có chiều dài từ 1 đến 5 kí tự bao gồm chữ thường, ký tự số, dấu chấm, dấu gạch dưới nhưng không được kết thúc bằng dấu chấm.

**<u>Ví dụ:</u>**
- *duy.tran2903*, *duy.tran.3_12* là các chuỗi BKNetID hợp lệ.
- *duy.tran2903*. hoặc *duy2.tran2903* là BKNetID không hợp lệ.

Hãy sử dụng ANTLR để viết biểu thức chính quy cho **BKNetID** nói trên. Sinh viên phải sử dụng **fragment** để nhận trọn điểm.

**For example**:

| Test  | Result    |
|-------|-----------|
| duy.tran2903 | duy.tran2903,<EOF> |

**Answer**:
```antlr
BKID: NAME '.' NAME OPTION;
fragment NAME: [a-z]+;
fragment OPTION: CHAR? CHAR? CHAR? CHAR? [a-z0-9_];
fragment CHAR: [a-z0-9._];
```

## Exercise 5
Use ANTLR to write regular expressions describing a valid IPv4 address. It consists of exact 4 strings, whose length is from 1 to 3, of digits (0-9) but not starting with 0 unless the string is 0. The strings are separated by one dot (.).

**For example**:
| Test  | Result    |
|-------|-----------|
| 192.168.0.1 | 192.168.0.1,<EOF> |

**Answer**:
```antlr
IPV4: STR '.' STR '.' STR '.' STR;
fragment STR: '0' | [1-9] DIGIT? DIGIT?;
fragment DIGIT: [0-9];
```

## Exercise 6
Use ANTLR to write regular expressions describing PHP's integers (in decimal) which is a sequence of digits (0-9) starting with a non-zero digit or only a zero. Integer literals may contain underscores (_) between digits, for better readability of literals but these underscores are removed by PHP's scanner.

**For example**:
| Test  | Result    |
|-------|-----------|
| 1_234_567 | 1234567,<EOF> |

**Answer**:
```antlr
PHPINT: '0' | [1-9] ('_'? [0-9])* {self.text = self.text.replace("_", "")};
```

## Exercise 7
Hãy dùng ANTLR để viết biểu thức chính qui cho token SHEXA mô tả các chuỗi số thập lục phân thoả mãn tất cả các yêu cầu sau:
- không rỗng
- tương ứng với một số nguyên chẵn
- có ký tự đầu tiên chỉ gồm các ký tự số
- không phân biệt chữ thường và hoa
- không sử dụng action khi viết biểu thức chính qui cho SHEXA

Ví dụ: các chuỗi hợp lệ với SHEXA: 12, 21A, 3dC, 2.  
Các chuỗi không hợp lệ với SHEXA: A12 (ký tự đầu tiên là chữ), 1B (ứng với 27 không phải là số nguyên chẵn).

**For example**:
| Test  | Result    |
|-------|-----------|
| 12 | 12,<EOF> |

**Answer**:
```antlr
SHEXA: [1-9] [0-9a-fA-F]* [02468aAcCeE];
```