# Advent of Code 2025 - Day 3 Part 2: Lobby

#' Find maximum joltage by selecting exactly k batteries
#'
#' @param bank_string A string of digits representing battery joltages
#' @param k Number of batteries to select (12 for Part 2)
#' @return The maximum joltage possible as a numeric value
find_max_joltage_k_batteries <- function(bank_string, k = 12) {
  # Convert string to vector of digits
  digits <- as.integer(strsplit(bank_string, "")[[1]])
  n <- length(digits)
  
  # If we need more batteries than available, return 0
  if (k > n) {
    return(0)
  }
  
  # If k equals n, return all digits
  if (k == n) {
    return(as.numeric(bank_string))
  }
  
  # We need to select k positions out of n
  # To maximize, use greedy algorithm:
  # At each position, pick the largest digit that still leaves
  # enough digits remaining to complete the selection
  
  selected_indices <- integer(k)
  last_index <- 0  # Last selected index
  
  for (pos in 1:k) {
    # How many more digits do we need after this one?
    remaining_needed <- k - pos
    
    # We can look ahead up to position: n - remaining_needed
    search_end <- n - remaining_needed
    
    # Find the maximum digit in the valid range
    search_start <- last_index + 1
    valid_range <- search_start:search_end
    
    # Find which index has the maximum digit
    max_digit <- -1
    best_idx <- search_start
    
    for (idx in valid_range) {
      if (digits[idx] > max_digit) {
        max_digit <- digits[idx]
        best_idx <- idx
      }
    }
    
    selected_indices[pos] <- best_idx
    last_index <- best_idx
  }
  
  # Build the number from selected digits
  selected_digits <- digits[selected_indices]
  result_string <- paste(selected_digits, collapse = "")
  
  # Convert to numeric (using as.numeric for large numbers)
  # Note: For very large numbers, R will use scientific notation
  # We'll return as character to preserve precision, then sum as numeric
  return(as.numeric(result_string))
}


#' Solve Day 3 Part 2
#'
#' @param input_file Path to input file
#' @return Total output joltage
solve_day3_part2 <- function(input_file = "input.txt") {
  # Read input lines
  banks <- readLines(input_file)
  
  # Find maximum joltage for each bank (12 batteries)
  max_joltages <- sapply(banks, function(bank) {
    find_max_joltage_k_batteries(bank, k = 12)
  })
  
  # Sum all maximum joltages
  total_joltage <- sum(max_joltages)
  
  return(total_joltage)
}


#' Test with example
test_example_part2 <- function() {
  example_banks <- c(
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
  )
  
  cat("Testing Part 2 with example:\n")
  
  expected_results <- c(987654321111, 811111111119, 434234234278, 888911112111)
  
  for (i in seq_along(example_banks)) {
    bank <- example_banks[i]
    max_jolt <- find_max_joltage_k_batteries(bank, k = 12)
    cat(sprintf("  %s -> %.0f (expected: %.0f) %s\n", 
                bank, max_jolt, expected_results[i],
                ifelse(max_jolt == expected_results[i], "✓", "✗")))
  }
  
  total <- sum(sapply(example_banks, function(b) {
    find_max_joltage_k_batteries(b, k = 12)
  }))
  
  cat(sprintf("\nTotal: %.0f (expected: 3121910778619)\n\n", total))
}


#' Combined solution for both parts
solve_day3 <- function(input_file = "input.txt") {
  # Part 1: Select 2 batteries
  find_max_joltage_part1 <- function(bank_string) {
    digits <- as.integer(strsplit(bank_string, "")[[1]])
    n <- length(digits)
    max_joltage <- 0
    
    for (i in 1:(n - 1)) {
      for (j in (i + 1):n) {
        joltage <- digits[i] * 10 + digits[j]
        max_joltage <- max(max_joltage, joltage)
      }
    }
    return(max_joltage)
  }
  
  # Read input
  banks <- readLines(input_file)
  
  # Solve Part 1
  part1_joltages <- sapply(banks, find_max_joltage_part1)
  part1_total <- sum(part1_joltages)
  
  # Solve Part 2
  part2_joltages <- sapply(banks, function(b) {
    find_max_joltage_k_batteries(b, k = 12)
  })
  part2_total <- sum(part2_joltages)
  
  list(
    part1 = part1_total,
    part2 = part2_total
  )
}


# Main execution
main <- function() {
  # Test with example
  test_example_part2()

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
    results <- solve_day3(input_file)
    cat(sprintf("Part 1 Answer: %.0f\n", results$part1))
    cat(sprintf("Part 2 Answer: %.0f\n", results$part2))
  } else {
    cat("Error: input.txt not found in any of the expected locations:\n")
    for (p in candidates) cat(sprintf("  - %s\n", p))
    cat("Please create input.txt with your puzzle input in the script directory or working directory.\n")
  }
}

# Run the solution
main()