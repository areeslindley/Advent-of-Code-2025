# Advent of Code 2025 - Day 3: Lobby
# Find maximum joltage from battery banks

#' Find maximum joltage from a single bank
#'
#' @param bank_string A string of digits representing battery joltages
#' @return The maximum joltage (two-digit number) possible
find_max_joltage <- function(bank_string) {
  # Convert string to vector of digits
  digits <- as.integer(strsplit(bank_string, "")[[1]])
  n <- length(digits)
  
  # If less than 2 batteries, return 0 (shouldn't happen with valid input)
  if (n < 2) {
    return(0)
  }
  
  max_joltage <- 0
  
  # Try all pairs of positions (i, j) where i < j
  for (i in 1:(n - 1)) {
    for (j in (i + 1):n) {
      # Form the two-digit number from positions i and j
      joltage <- digits[i] * 10 + digits[j]
      max_joltage <- max(max_joltage, joltage)
    }
  }
  
  return(max_joltage)
}


#' Solve Day 3 Part 1
#'
#' @param input_file Path to input file
#' @return Total output joltage
solve_day3_part1 <- function(input_file = "input.txt") {
  # Read input lines
  banks <- readLines(input_file)
  
  # Find maximum joltage for each bank
  max_joltages <- sapply(banks, find_max_joltage)
  
  # Sum all maximum joltages
  total_joltage <- sum(max_joltages)
  
  return(total_joltage)
}


#' Test with example
test_example <- function() {
  example_banks <- c(
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
  )
  
  cat("Testing with example:\n")
  
  for (bank in example_banks) {
    max_jolt <- find_max_joltage(bank)
    cat(sprintf("  %s -> %d\n", bank, max_jolt))
  }
  
  total <- sum(sapply(example_banks, find_max_joltage))
  cat(sprintf("\nTotal: %d (expected: 357)\n\n", total))
}


# Main execution
main <- function() {
  # Test with example
  test_example()

  # Determine script directory (works when run with Rscript)
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- "--file="
  script_path <- NULL
  idx <- grep(file_arg, args)
  if (length(idx) > 0) {
    script_path <- sub(file_arg, "", args[idx][1])
  }

  if (is.null(script_path) || script_path == "") {
    script_dir <- getwd()
  } else {
    # Remove surrounding quotes if present and expand ~
    script_path <- gsub("^['\"]|['\"]$", "", script_path)
    script_path <- path.expand(script_path)
    # Try to normalize path (suppress warnings); if it fails, fall back to the expanded path
    safe_norm <- tryCatch(suppressWarnings(normalizePath(script_path)), error = function(e) script_path)
    script_dir <- dirname(safe_norm)
  }

  # Candidate input file locations (script dir, working dir, common fallback)
  candidates <- c(
    file.path(script_dir, "input.txt"),
    file.path(getwd(), "input.txt"),
    path.expand("~/Documents/Code/Advent of Code 2025/Day 3/input.txt")
  )

  input_file <- NULL
  for (p in candidates) {
    if (file.exists(p)) {
      input_file <- p
      break
    }
  }

  if (!is.null(input_file)) {
    answer <- solve_day3_part1(input_file)
    cat(sprintf("Part 1 Answer: %d\n", answer))
  } else {
    cat("Error: input.txt not found in any of the expected locations:\n")
    for (p in candidates) cat(sprintf("  - %s\n", p))
    cat("Please create input.txt with your puzzle input in the script directory or working directory.\n")
  }
}

# Run the solution
main()