namespace PiSync.Home
{
    partial class HomeForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            btnLogout = new Button();
            btnTenants = new Button();
            btnRooms = new Button();
            btnDashboard = new Button();
            panel2 = new Panel();
            label3 = new Label();
            mainPanel = new Panel();
            panel1.SuspendLayout();
            panel2.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.GhostWhite;
            panel1.Controls.Add(btnLogout);
            panel1.Controls.Add(btnTenants);
            panel1.Controls.Add(btnRooms);
            panel1.Controls.Add(btnDashboard);
            panel1.Controls.Add(panel2);
            panel1.Dock = DockStyle.Left;
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(241, 518);
            panel1.TabIndex = 1;
            // 
            // btnLogout
            // 
            btnLogout.Anchor = AnchorStyles.Bottom | AnchorStyles.Left;
            btnLogout.BackColor = Color.Lavender;
            btnLogout.Cursor = Cursors.Hand;
            btnLogout.FlatAppearance.BorderSize = 0;
            btnLogout.FlatStyle = FlatStyle.Flat;
            btnLogout.Font = new Font("Courier New", 14F);
            btnLogout.Location = new Point(12, 440);
            btnLogout.Margin = new Padding(0);
            btnLogout.Name = "btnLogout";
            btnLogout.Size = new Size(212, 61);
            btnLogout.TabIndex = 4;
            btnLogout.Text = "LOGOUT";
            btnLogout.UseVisualStyleBackColor = true;
            // 
            // btnTenants
            // 
            btnTenants.BackColor = Color.Lavender;
            btnTenants.Cursor = Cursors.Hand;
            btnTenants.FlatAppearance.BorderSize = 0;
            btnTenants.FlatStyle = FlatStyle.Flat;
            btnTenants.Font = new Font("Courier New", 14F);
            btnTenants.Location = new Point(12, 239);
            btnTenants.Margin = new Padding(0);
            btnTenants.Name = "btnTenants";
            btnTenants.Size = new Size(212, 61);
            btnTenants.TabIndex = 3;
            btnTenants.Text = "TENANTS";
            btnTenants.UseVisualStyleBackColor = true;
            // 
            // btnRooms
            // 
            btnRooms.BackColor = Color.Lavender;
            btnRooms.Cursor = Cursors.Hand;
            btnRooms.FlatAppearance.BorderSize = 0;
            btnRooms.FlatStyle = FlatStyle.Flat;
            btnRooms.Font = new Font("Courier New", 14F);
            btnRooms.Location = new Point(12, 167);
            btnRooms.Margin = new Padding(0);
            btnRooms.Name = "btnRooms";
            btnRooms.Size = new Size(212, 61);
            btnRooms.TabIndex = 2;
            btnRooms.Text = "ROOMS";
            btnRooms.UseVisualStyleBackColor = true;
            // 
            // btnDashboard
            // 
            btnDashboard.BackColor = Color.Lavender;
            btnDashboard.Cursor = Cursors.Hand;
            btnDashboard.FlatAppearance.BorderSize = 0;
            btnDashboard.FlatStyle = FlatStyle.Flat;
            btnDashboard.Font = new Font("Courier New", 14F);
            btnDashboard.Location = new Point(12, 96);
            btnDashboard.Margin = new Padding(0);
            btnDashboard.Name = "btnDashboard";
            btnDashboard.Size = new Size(212, 61);
            btnDashboard.TabIndex = 1;
            btnDashboard.Text = "DASHBOARD";
            btnDashboard.UseVisualStyleBackColor = true;
            // 
            // panel2
            // 
            panel2.BackColor = Color.MediumPurple;
            panel2.Controls.Add(label3);
            panel2.Dock = DockStyle.Top;
            panel2.Location = new Point(0, 0);
            panel2.Name = "panel2";
            panel2.Size = new Size(241, 79);
            panel2.TabIndex = 0;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Courier New", 16F);
            label3.ForeColor = Color.Lavender;
            label3.Location = new Point(59, 24);
            label3.Name = "label3";
            label3.Size = new Size(109, 30);
            label3.TabIndex = 1;
            label3.Text = "PISYNC";
            // 
            // mainPanel
            // 
            mainPanel.BackColor = SystemColors.HighlightText;
            mainPanel.Dock = DockStyle.Fill;
            mainPanel.Location = new Point(241, 0);
            mainPanel.Name = "mainPanel";
            mainPanel.Size = new Size(700, 518);
            mainPanel.TabIndex = 2;
            // 
            // HomeForm
            // 
            AutoScaleDimensions = new SizeF(14F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(941, 518);
            Controls.Add(mainPanel);
            Controls.Add(panel1);
            Font = new Font("Courier New", 13.8F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(5, 4, 5, 4);
            Name = "HomeForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "HomeForm";
            panel1.ResumeLayout(false);
            panel2.ResumeLayout(false);
            panel2.PerformLayout();
            ResumeLayout(false);
        }

        #endregion
        private Panel panel1;
        private Panel panel2;
        private Button btnDashboard;
        private Label label3;
        private Button btnTenants;
        private Button btnRooms;
        private Panel mainPanel;
        private Button btnLogout;
    }
}