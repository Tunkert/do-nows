<?php
function create_number() {
    $random_number = rand(1, 12);
    $random_number_sign = rand(1, 2);
    if ($random_number_sign === 1) {
        $random_number *= -1;
    } 
    return $random_number;
};

function create_quadratic() {
    $a = create_number();
    $b = create_number();
    $c = create_number();
    while ($b * $b - 4 * $a * $c >= 0) {
        $a = create_number();
        $b = create_number();
        $c = create_number();
    }
    return "<p>\\(" . "$a" . "x^2 + $b" .  "x + $c = 0 \\)</p>";
};

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quadratic Formula Complex Solutions</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        .container {
            margin: 0 0.5in;
        }

        .row {
            display: flex;
            justify-content: space-between;
            min-height: 420px;
        }

        .problem {
            width: 45%;
        }

        .pb {
            page-break-after: always;
        }
    </style>
</head>
<body>
    <div class="container">
        <?php 
        echo "\n<p>Solve the following equations using the Quadratic Formula.</p>\n";
        for ($i = 0; $i < 4; $i++) {
            echo "\n<div class='row'>\n";
            echo "<div class='problem'>\n";
            $problem = create_quadratic();
            echo "\n<h2>Problem " . 2 * $i + 1 . "</h2>\n";
            echo $problem;
            echo "\n</div>\n";
            echo "<div class='problem'>\n";
            $problem = create_quadratic();
            echo "\n<h2>Problem " . 2 * $i + 2 . "</h2>\n";
            echo $problem;
            echo "\n</div>\n";
            echo "</div>\n";
            if ((($i + 1) % 2 === 0) && ($i < 3)) {
                echo "\n<div class='pb'></div>\n";
            };
        };

        ?>

        <script>
            let refreshPage = () => {
                location.reload();
            }
        </script>
        <button onclick="refreshPage();">Refresh Page</button>
    </div>
</body>
</html>